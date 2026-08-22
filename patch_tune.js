// --- Advanced Audio System (Improved IPL Tune) ---
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
const GLOBAL_VOLUME = 0.15; // Slightly bumped up but still soft

function playHornTone(freq, duration, delay) {
    if(audioCtx.state === 'suspended') return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();
    
    // Trumpet-like settings
    osc.type = 'sawtooth';
    filter.type = 'lowpass';
    
    // Brass filter envelope
    filter.frequency.setValueAtTime(500, audioCtx.currentTime + delay);
    filter.frequency.linearRampToValueAtTime(3000, audioCtx.currentTime + delay + 0.05);
    filter.frequency.linearRampToValueAtTime(1000, audioCtx.currentTime + delay + duration);
    
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime + delay);
    
    // Volume envelope (ADSR)
    gain.gain.setValueAtTime(0, audioCtx.currentTime + delay);
    gain.gain.linearRampToValueAtTime(1.0 * GLOBAL_VOLUME, audioCtx.currentTime + delay + 0.03); // Attack
    gain.gain.linearRampToValueAtTime(0.8 * GLOBAL_VOLUME, audioCtx.currentTime + delay + 0.1);  // Decay
    gain.gain.setValueAtTime(0.8 * GLOBAL_VOLUME, audioCtx.currentTime + delay + duration - 0.05); // Sustain
    gain.gain.linearRampToValueAtTime(0, audioCtx.currentTime + delay + duration); // Release
    
    osc.connect(filter);
    filter.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start(audioCtx.currentTime + delay);
    osc.stop(audioCtx.currentTime + delay + duration);
}

function playSoldSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    
    // Heavy Gavel Thud (SOLD!)
    const thud = audioCtx.createOscillator();
    const gainThud = audioCtx.createGain();
    thud.type = 'sine';
    thud.frequency.setValueAtTime(150, audioCtx.currentTime);
    thud.frequency.exponentialRampToValueAtTime(10, audioCtx.currentTime + 0.15);
    gainThud.gain.setValueAtTime(1.5 * GLOBAL_VOLUME, audioCtx.currentTime);
    gainThud.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.15);
    thud.connect(gainThud);
    gainThud.connect(audioCtx.destination);
    thud.start();
    thud.stop(audioCtx.currentTime + 0.15);

    // The Famous Stadium "Charge!" Fanfare
    // Notes: G4, C5, E5, G5... E5, G5!
    playHornTone(392.00, 0.15, 0.2); // G4
    playHornTone(523.25, 0.15, 0.35); // C5
    playHornTone(659.25, 0.15, 0.5); // E5
    playHornTone(783.99, 0.3, 0.65); // G5
    playHornTone(659.25, 0.15, 1.0); // E5
    playHornTone(783.99, 0.5, 1.15); // G5 (Hold)
}

function playBidSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    // Clean, crisp digital bell
    osc.type = 'sine';
    osc.frequency.setValueAtTime(1800, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(600, audioCtx.currentTime + 0.15);
    
    gain.gain.setValueAtTime(0.6 * GLOBAL_VOLUME, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.15);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.15);
}

function playUnsoldSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(150, audioCtx.currentTime);
    osc.frequency.linearRampToValueAtTime(80, audioCtx.currentTime + 0.6);
    
    gain.gain.setValueAtTime(0.4 * GLOBAL_VOLUME, audioCtx.currentTime);
    gain.gain.linearRampToValueAtTime(0, audioCtx.currentTime + 0.6);
    
    // Add a lowpass filter to make it sound muffled/sad
    const filter = audioCtx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(800, audioCtx.currentTime);
    filter.frequency.linearRampToValueAtTime(200, audioCtx.currentTime + 0.6);
    
    osc.connect(filter);
    filter.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.6);
}

function playTickSound() {
    if(audioCtx.state === 'suspended') return;
    
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    // Wooden clock tick
    osc.type = 'square';
    osc.frequency.setValueAtTime(800, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.05);
    
    gain.gain.setValueAtTime(0.3 * GLOBAL_VOLUME, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.05);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.05);
}
