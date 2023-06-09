const MongoClient = require('mongodb').MongoClient;

// Replace the URL with your own MongoDB Atlas connection string
const url = 'mongodb+srv://tanviropy:tanviropy@cluster0.lftvw.mongodb.net/testing?retryWrites=true&w=majority';

const dbName = 'BD-Cuisine';

async function connect() {
    const client = await MongoClient.connect(url, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    });
    const db = client.db(dbName);
    return db;
}

module.exports = { connect };