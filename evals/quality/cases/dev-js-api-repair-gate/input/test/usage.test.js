const assert = require("assert");
const { calculateRemainingBudget, shouldThrottle } = require("../src/usage");

assert.strictEqual(calculateRemainingBudget({ plan: "team", units: "500" }), 24500);
assert.strictEqual(shouldThrottle({ plan: "enterprise", units: 249999 }), false);
assert.strictEqual(shouldThrottle({ plan: "starter", units: 1000 }), true);
assert.throws(() => calculateRemainingBudget({ plan: "unknown", units: 1 }), /unknown plan/);
assert.throws(() => calculateRemainingBudget({ plan: "team", units: -1 }), /non-negative/);

console.log("usage tests passed");
