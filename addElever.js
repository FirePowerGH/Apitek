import { fakerNB_NO } from '@faker-js/faker';
import mysql from 'mysql2';
import dotenv from 'dotenv';

dotenv.config()

const db = mysql.createPool({
    host: process.env.sqlHost,
    user: process.env.sqlUser,
    password: process.env.sqlPass,
    database: process.env.sqlDb,
}).promise()

let fornavn = fakerNB_NO.person.firstName();
let etternavn = fakerNB_NO.person.lastName();

let navn = fornavn + " " + etternavn;
console.log(navn);

async function elever(fornavn, etternavn) {
    const [result] = await db.query(`
        INSERT INTO elever (fornavn, etternavn)
        VALUES (?, ?)` [fornavn, etternavn])

    const id = result.insertId
}

elever(fornavn, etternavn)