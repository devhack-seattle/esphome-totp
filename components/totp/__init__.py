#!/usr/bin/env python

import logging
from importlib import resources
from typing import Optional

import tzlocal

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation
from esphome.const import (
    CONF_ID,
    CONF_CRON,
    CONF_DAYS_OF_MONTH,
    CONF_DAYS_OF_WEEK,
    CONF_HOURS,
    CONF_MINUTES,
    CONF_MONTHS,
    CONF_ON_TIME,
    CONF_ON_TIME_SYNC,
    CONF_SECONDS,
    CONF_TIMEZONE,
    CONF_TRIGGER_ID,
    CONF_AT,
    CONF_SECOND,
    CONF_HOUR,
    CONF_MINUTE,
)
from esphome.core import coroutine_with_priority
from esphome.automation import Condition

_LOGGER = logging.getLogger(__name__)

CODEOWNERS = ["@mjsir911"]
IS_PLATFORM_COMPONENT = False

totp_ns = cg.esphome_ns.namespace("totp")
TOTPComponent = totp_ns.class_("TOTPComponent", cg.Component)


from esphome.components import time

CONFIG_SCHEMA = cv.All(
    cv.COMPONENT_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(TOTPComponent),
            cv.Required("clock_id"): cv.use_id(time.RealTimeClock),
            cv.Required("hmacKey"): cv.string,  # base64
            cv.Optional("timeStep", 30): cv.int_,
        }
    )
)


async def to_code(config):
    cg.add_library("TOTP library", None)

    import base64
    decoded_key = base64.b32decode(config['hmacKey'])

    var = cg.new_Pvariable(config[CONF_ID], list(decoded_key), config['timeStep'])

    time_source = await cg.get_variable(config["clock_id"])
    cg.add(var.set_clock(time_source))


    await cg.register_component(var, config)
