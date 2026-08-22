
const iplHornAudio = new Audio('/static/ipl_horn.webm');
iplHornAudio.volume = 0.15; // Kept at low volume

function playSoldSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    
    // Play official IPL horn MP3/WEBM
    iplHornAudio.currentTime = 0;
    iplHornAudio.play().catch(e => console.log('Audio play failed:', e));
    
    // Cut it off after 4 seconds in case the clip is too long
    setTimeout(() => {
        iplHornAudio.pause();
        iplHornAudio.currentTime = 0;
    }, 4000);
    
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
}
