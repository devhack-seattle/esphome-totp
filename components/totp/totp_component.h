#pragma once

#include "esphome/core/component.h"
#include "TOTP.h"
#include "esphome/components/time/real_time_clock.h"

namespace esphome {
namespace totp {

class TOTPComponent : public Component {
 public:
  TOTPComponent(const std::vector<uint8_t> &hmacKey, int timestep) : hmacKey_(hmacKey), totp(hmacKey_.data(), hmacKey_.size(), timestep) {};

  void set_clock(time::RealTimeClock *clock) {
      this->clock = clock;
  }

  char *getCode();

 protected:
  std::vector<uint8_t> hmacKey_;
  TOTP totp;

  time::RealTimeClock *clock;
};

}  // namespace sntp
}  // namespace esphome

