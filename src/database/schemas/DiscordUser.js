const mongoose = require('mongoose');

const DiscordUserSchema = new mongoose.Schema({
    discordId: {
        type:mongoose.SchemaTypes.String,
        require:true,
    },
    createAt: {
        type:mongoose.SchemaTypes.Date,
        require:true,
        default: new Date(),
    },
});

module.exports = mongoose.model('discord_users', DiscordUserSchema);