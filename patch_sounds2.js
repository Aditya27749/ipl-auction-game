
// --- Advanced Audio System (IPL Style - Low Volume) ---
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

const GLOBAL_VOLUME = 0.1; // Extremely low, subtle volume

function playTone(freq, type, duration, vol=0.5, delay=0) {
    if(audioCtx.state === 'suspended') return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime + delay);
    
    // Smooth envelope to avoid clicks
    gain.gain.setValueAtTime(0, audioCtx.currentTime + delay);
    gain.gain.linearRampToValueAtTime(vol * GLOBAL_VOLUME, audioCtx.currentTime + delay + 0.05);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + delay + duration);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(audioCtx.currentTime + delay);
    osc.stop(audioCtx.currentTime + delay + duration);
}

// "SOLD" - Stadium Horn Arpeggio (IPL Style) + Gavel Thud
function playSoldSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    
    // Gavel Thud
    const thud = audioCtx.createOscillator();
    const gainThud = audioCtx.createGain();
    thud.type = 'sine';
    thud.frequency.setValueAtTime(120, audioCtx.currentTime);
    thud.frequency.exponentialRampToValueAtTime(10, audioCtx.currentTime + 0.1);
    gainThud.gain.setValueAtTime(1.0 * GLOBAL_VOLUME, audioCtx.currentTime);
    gainThud.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
    thud.connect(gainThud);
    gainThud.connect(audioCtx.destination);
    thud.start();
    thud.stop(audioCtx.currentTime + 0.1);

    // Trumpet Fanfare (Sawtooth wave for brassy sound)
    // Notes: C5, E5, G5, C6
    playTone(523.25, 'sawtooth', 0.2, 0.4, 0.1); // C5
    playTone(659.25, 'sawtooth', 0.2, 0.4, 0.2); // E5
    playTone(783.99, 'sawtooth', 0.2, 0.4, 0.3); // G5
    playTone(1046.50, 'sawtooth', 0.6, 0.5, 0.4); // C6
}

// "Bidding" - Subtle coin click / ping
function playBidSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    osc.type = 'sine';
    osc.frequency.setValueAtTime(1500, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(500, audioCtx.currentTime + 0.1);
    
    gain.gain.setValueAtTime(0.5 * GLOBAL_VOLUME, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.1);
}

// "Unsold" - Low disappointing hum
function playUnsoldSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    playTone(150, 'sawtooth', 0.8, 0.5, 0);
    playTone(100, 'sawtooth', 0.8, 0.5, 0.2);
}

// "Countdown Tick" - Soft wooden block
function playTickSound() {
    if(audioCtx.state === 'suspended') return;
    
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(600, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.05);
    
    gain.gain.setValueAtTime(0.3 * GLOBAL_VOLUME, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.05);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.05);
}

