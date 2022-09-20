const express = require('express');

const controller = require('../controller/calculadora')

const router = express.Router()

const path = 'calculadora'

router.get('/' + path, controller.getData)



module.exports = router; //Exportame todo esto para llamarlo en otro archivo