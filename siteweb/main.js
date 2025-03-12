// script.js
import * as THREE from 'three';
import { FontLoader } from 'three/addons/loaders/FontLoader.js';
import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';

let camera, scene, renderer;
let textMesh;
let pointLight;

init();
animate();

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

    // Création du texte 3D
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

function onMouseMove(event) {
    const mouseX = (event.clientX / window.innerWidth) * 2 - 1;
    const mouseY = -(event.clientY / window.innerHeight) * 2 + 1;

    if (textMesh) {
        textMesh.rotation.x = mouseY * 0.1;
        textMesh.rotation.y = mouseX * 0.1;
    }

    pointLight.position.x = mouseX * 5;
    pointLight.position.y = mouseY * 5;
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