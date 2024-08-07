#include "totp_component.h"
#include "esphome/core/log.h"
#include "TOTP.h"

namespace esphome {
namespace totp {

static const char *const TAG = "totp";


char *TOTPComponent::getCode() {
    return this->totp.getCode(this->clock->timestamp_now());
}

}  // namespace totp
}  // namespace esphome

