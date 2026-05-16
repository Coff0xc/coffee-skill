const PLAN_LIMITS = {
  starter: 1000,
  team: 25000,
  enterprise: 250000,
};

function normalizeUsageEvent(event) {
  if (!event || typeof event !== "object") {
    throw new TypeError("event must be an object");
  }
  const plan = String(event.plan || "").toLowerCase();
  if (!Object.prototype.hasOwnProperty.call(PLAN_LIMITS, plan)) {
    throw new Error(`unknown plan: ${event.plan}`);
  }
  const units = Number(event.units);
  if (!Number.isFinite(units) || units < 0) {
    throw new Error("units must be a non-negative number");
  }
  return {
    accountId: String(event.accountId || "").trim(),
    plan,
    units,
    limit: PLAN_LIMITS[plan],
  };
}

function calculateRemainingBudget(event) {
  const normalized = normalizeUsageEvent(event);
  return Math.max(0, normalized.limit - normalized.units);
}

function shouldThrottle(event) {
  const normalized = normalizeUsageEvent(event);
  return normalized.units >= normalized.limit;
}

module.exports = {
  PLAN_LIMITS,
  normalizeUsageEvent,
  calculateRemainingBudget,
  shouldThrottle,
};
