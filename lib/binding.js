const addon = require('../build/Release/arl-dilithium-native');

module.exports = {
    generateKeypair: addon.generateKeypair,
    generateKeypairRandom: addon.generateKeypairRandom,
    sign: addon.sign,
    verify: addon.verify,
    privToPub: addon.privToPub,
};
