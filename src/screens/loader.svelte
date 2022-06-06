<div class="loader">
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; display: block; shape-rendering: auto;" width="200px" height="200px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
        <circle cx="50" cy="50" r="32" stroke-width="8" stroke="#df1317" stroke-dasharray="50.26548245743669 50.26548245743669" fill="none" stroke-linecap="round">
            <!-- <animateTransform attributeName="transform" type="rotate" repeatCount="indefinite" dur="1s" keyTimes="0;1" values="0 50 50;360 50 50"></animateTransform> -->
        </circle>
    </svg>
</div>

<style>
    .loader {
        position: fixed;
        top: 0;
		left: 0;
		right: 0;
		bottom: 0;
        display: grid;
        place-items: center;
		animation-name: ckw;
		animation-duration: 1s;
		animation-iteration-count: infinite;
    }
    
    @keyframes ckw {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
</style>