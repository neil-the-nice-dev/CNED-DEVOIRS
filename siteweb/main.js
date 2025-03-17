// script.js
import * as THREE from 'three';
import { FontLoader } from 'three/addons/loaders/FontLoader.js';
import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

let camera, scene, renderer;
let textMesh;
let pointLight;

init();
animate();
initScrollAnimations();

function init() {
    // Configuration de base
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 15;

    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('container').appendChild(renderer.domElement);

    // Éclairage
    const ambientLight = new THREE.AmbientLight(0x404040, 2);
    scene.add(ambientLight);

    pointLight = new THREE.PointLight(0x4444ff, 15);
    pointLight.position.set(2, 3, 4);
    scene.add(pointLight);

    const loader = new THREE.FontLoader();
    loader.load('https://threejs.org/examples/fonts/helvetiker_bold.typeface.json', function(font) {
        const textGeometry = new THREE.TextGeometry('NEIL TORNER', {
            font: font,
            size: 1.5,
            height: 0.2,
            curveSegments: 12,
            bevelEnabled: true,
            bevelThickness: 0.03,
            bevelSize: 0.02,
            bevelOffset: 0,
            bevelSegments: 5
        });

        const textMaterial = new THREE.MeshStandardMaterial({
            color: 0xffffff,
            metalness: 0.8,
            roughness: 0.2
        });

        textMesh = new THREE.Mesh(textGeometry, textMaterial);
        textGeometry.center();
        scene.add(textMesh);

        // Animation initiale du texte
        gsap.from(textMesh.position, {
            y: -20,
            duration: 2,
            ease: "power4.out"
        });
    });

    // Particules d'arrière-plan
    const particlesGeometry = new THREE.BufferGeometry();
    const particlesCount = 5000;
    const posArray = new Float32Array(particlesCount * 3);
    
    for(let i = 0; i < particlesCount * 3; i++) {
        posArray[i] = (Math.random() - 0.5) * 50;
    }
    
    particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
    const particlesMaterial = new THREE.PointsMaterial({
        size: 0.02,
        color: 0x4444ff,
        transparent: true,
        opacity: 0.8
    });
    
    const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
    scene.add(particlesMesh);

    // Événements
    window.addEventListener('resize', onWindowResize, false);
    document.addEventListener('mousemove', onMouseMove);
}

function initScrollAnimations() {
    // Animation des sections au défilement
    gsap.utils.toArray('.section').forEach((section, i) => {
        gsap.from(section, {
            scrollTrigger: {
                trigger: section,
                start: "top center",
                toggleActions: "play none none reverse"
            },
            opacity: 0,
            y: 50,
            duration: 1,
            ease: "power2.out"
        });
    });

    // Animation des compétences
    gsap.utils.toArray('.skills span').forEach((skill, i) => {
        gsap.from(skill, {
            scrollTrigger: {
                trigger: skill,
                start: "top bottom",
                toggleActions: "play none none reverse"
            },
            opacity: 0,
            y: 20,
            duration: 0.6,
            delay: i * 0.1
        });
    });
}

function onMouseMove(event) {
    const mouseX = (event.clientX / window.innerWidth) * 2 - 1;
    const mouseY = -(event.clientY / window.innerHeight) * 2 + 1;

    if (textMesh) {
        gsap.to(textMesh.rotation, {
            x: mouseY * 0.1,
            y: mouseX * 0.1,
            duration: 0.5
        });
    }

    gsap.to(pointLight.position, {
        x: mouseX * 5,
        y: mouseY * 5,
        duration: 0.2
    });
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
    requestAnimationFrame(animate);

    if (textMesh) {
        textMesh.rotation.y += 0.001;
    }

    renderer.render(scene, camera);
}

// Attendre que le DOM soit chargé
document.addEventListener('DOMContentLoaded', () => {
    // Initialiser GSAP
    gsap.registerPlugin(ScrollTrigger);

    // Masquer le texte "Move your mouse"
    const splineViewer = document.querySelector('spline-viewer');
    if (splineViewer) {
        splineViewer.addEventListener('load', () => {
            const shadowRoot = splineViewer.shadowRoot;
            if (shadowRoot) {
                setTimeout(() => {
                    const moveText = shadowRoot.querySelector('.text');
                    if (moveText) {
                        moveText.style.display = 'none';
                    }
                }, 100);
            }
        });
    }

    // Animations d'entrée
    gsap.from('.title-wrapper', {
        opacity: 0,
        y: 30,
        duration: 1,
        ease: 'power3.out',
        delay: 0.5
    });

    gsap.from('.skills-wrapper', {
        opacity: 0,
        y: 30,
        duration: 1,
        ease: 'power3.out',
        delay: 0.8
    });

    // Animation des sections au scroll
    gsap.utils.toArray('.content-section').forEach(section => {
        gsap.from(section, {
            scrollTrigger: {
                trigger: section,
                start: 'top center',
                toggleActions: 'play none none reverse'
            },
            opacity: 0,
            y: 50,
            duration: 1,
            ease: 'power3.out'
        });
    });

    // Navigation active au scroll
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-links a');

    const observerOptions = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => observer.observe(section));

    // Smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Gestion du chargement de Spline
window.addEventListener('load', () => {
    const splineViewer = document.querySelector('spline-viewer');
    if (splineViewer) {
        splineViewer.addEventListener('load', () => {
            gsap.to(splineViewer, {
                opacity: 1,
                duration: 1,
                ease: "power2.out"
            });
        });
    }
});