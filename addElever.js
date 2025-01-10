import { fakerNB_NO } from '@faker-js/faker';
import mysql from 'mysql2';
import dotenv from 'dotenv';

dotenv.config()

const db = mysql.createPool({
    host: process.env.sqlHost,
    user: process.env.sqlUser,
    password: process.env.sqlPass,
    database: process.env.sqlDb
}).promise()

let fornavn = fakerNB_NO.person.firstName();
let etternavn = fakerNB_NO.person.lastName();

let navn = fornavn + " " + etternavn

function getRandomElement(list) {
    return list[Math.floor(Math.random() * list.length)];
}

function getProgramfag() {
    const vg1 = ["1IM", "1ST", "1MK"];
    const vg2 = ["2IT", "2MP", "2ST", "2MK"];
    const vg3 = ["3ST", "3MK"];

    let pf;
    if (Math.random() < 0.3) {
        pf = getRandomElement(vg1);
    } else if (Math.random() < 0.9) {
        pf = getRandomElement(vg2);
    } else {
        pf = getRandomElement(vg3);
    }
    console.log(pf)
    return(pf);
}

async function elever(fornavn, etternavn) {
    const programfag = getProgramfag()

    const [result] = await db.query(`
        INSERT INTO elever (fornavn, etternavn, programfag)
        VALUES (?, ?, ?)`, [fornavn, etternavn, programfag])
        
    const id = result.insertId
    console.log("Lagt inn "+navn+" i databasen.");
}

elever(fornavn, etternavn)
