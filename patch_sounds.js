
// --- Advanced Audio System ---
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

// Wooden Hammer / Gavel Strike for "SOLD"
function playSoldSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    
    // The "thud" (low frequency drum)
    const osc = audioCtx.createOscillator();
    const gainOsc = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(150, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
    
    gainOsc.gain.setValueAtTime(1, audioCtx.currentTime);
    gainOsc.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
    
    osc.connect(gainOsc);
    gainOsc.connect(audioCtx.destination);
    
    // The "wood smack" (filtered noise)
    const bufferSize = audioCtx.sampleRate * 0.1; // 100ms
    const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
        data[i] = Math.random() * 2 - 1;
    }
    
    const noise = audioCtx.createBufferSource();
    noise.buffer = buffer;
    
    const filter = audioCtx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(1000, audioCtx.currentTime);
    filter.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.1);
    
    const gainNoise = audioCtx.createGain();
    gainNoise.gain.setValueAtTime(1.5, audioCtx.currentTime);
    gainNoise.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
    
    noise.connect(filter);
    filter.connect(gainNoise);
    gainNoise.connect(audioCtx.destination);
    
    osc.start(audioCtx.currentTime);
    noise.start(audioCtx.currentTime);
    osc.stop(audioCtx.currentTime + 0.2);
}

// Sharp Bell / Ding for "Bidding"
function playBidSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    osc.type = 'sine';
    // Classic bell frequency
    osc.frequency.setValueAtTime(1200, audioCtx.currentTime);
    
    gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.3);
}

// Disappointing Buzz for "Unsold"
function playUnsoldSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(100, audioCtx.currentTime);
    osc.frequency.linearRampToValueAtTime(80, audioCtx.currentTime + 0.5);
    
    gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
    gain.gain.linearRampToValueAtTime(0.01, audioCtx.currentTime + 0.5);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.5);
}

// Clock Tick for Countdown
function playTickSound() {
    if(audioCtx.state === 'suspended') return; // Don't force resume on ticks to avoid lag
    
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    osc.type = 'square';
    osc.frequency.setValueAtTime(800, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.05);
    
    gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.05);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.05);
}

