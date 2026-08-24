const iplHornAudio = new Audio("/static/ipl_horn.webm");
iplHornAudio.volume = 0.15;

function playSoldSound() {
    if(audioCtx.state === "suspended") audioCtx.resume();
    iplHornAudio.currentTime = 0;
    iplHornAudio.play().catch(e => console.log("Audio play failed:", e));
    setTimeout(() => {
        iplHornAudio.pause();
        iplHornAudio.currentTime = 0;
    }, 4000);
    const thud = audioCtx.createOscillator();
    const gainThud = audioCtx.createGain();
    thud.type = "sine";
    thud.frequency.setValueAtTime(150, audioCtx.currentTime);
    thud.frequency.exponentialRampToValueAtTime(10, audioCtx.currentTime + 0.15);
    gainThud.gain.setValueAtTime(1.5 * GLOBAL_VOLUME, audioCtx.currentTime);
    gainThud.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.15);
    thud.connect(gainThud);
    gainThud.connect(audioCtx.destination);
    thud.start();
    thud.stop(audioCtx.currentTime + 0.15);
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
