import styled, { keyframes } from "styled-components";

export const spin = keyframes`
0% { transform: rotate(0deg); }
5%  {border: 5px solid #f3f3f3; border-top: 5px solid #33086d; }
45%  {border: 16px solid #f3f3f3; border-top: 16px solid #AE14C3; }
55%  {border: 16px solid #f3f3f3; border-top: 16px solid #AE14C3; }
95%  {border: 5px solid #f3f3f3; border-top: 5px solid #33086d; }
100% { transform: rotate(360deg); border: 5px solid #f3f3f3;
    border-top: 5px solid #33086d;}
`;

export const Loader = styled.div`
  border: 5px solid #f3f3f3; /* Light grey */
  border-top: 5px solid #33086d;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  animation: ${spin} 1s cubic-bezier(0, 0, 0.9, 1) infinite;
`;

export default Loader;
