const PLAN_LIMITS = {
  Starter: 1000,
  Team: 25000,
  Enterprise: 250000,
};

function calculateRemainingBudget(event) {
  return PLAN_LIMITS[event.plan] - event.units;
}

function shouldThrottle(event) {
  return calculateRemainingBudget(event) <= 0;
}

module.exports = {
  PLAN_LIMITS,
  calculateRemainingBudget,
  shouldThrottle,
};
