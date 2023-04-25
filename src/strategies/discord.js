const passport = require('passport');
const { Strategy } = require('passport-discord')
const DiscordUser = require('../database/schemas/DiscordUser')

passport.serializeUser((user, done) => {
    console.log('Serializing User...');
    console.log(user);
    done(null, user.id);
});

passport.deserializeUser(async (id, done) => {
    console.log('Deserializing User...')
    console.log(id);
    try {
        const user = await DiscordUser.findById(id);
        if (!user) throw new Error('User not found');
        console.log(user);
        done(null, user);
    } catch (error) {
        console.log(error);
        done(error, null);
    }
});

passport.use(
    new Strategy({
        clientID: process.env.DISCORD_OAUTH_CLIENT_ID,
        clientSecret: process.env.DISCORD_OAUTH_SECRET,
        callbackURL: process.env.DISCORD_REDIRECT_URL,
        scope: ['identify','guilds'],
    }, async (accessToken, refreshToken, profile, done) => {
        console.log(accessToken, refreshToken)
        console.log(profile)
        try {
            const discordUser = await DiscordUser.findOne({ 
                discordId: profile.id, 
            });
            if (discordUser) {
                console.log(`Found User: ${discordUser}`);
                return done(null, discordUser);
            }
            else {
                const newUser = await DiscordUser.create({
                    discordId: profile.id,
                });
                console.log(`Created User: ${newUser}`);
                return done(null, newUser);
            }
        } catch (error) {
            console.log(error);
            return done(error, null);
        }
    }
    )
);