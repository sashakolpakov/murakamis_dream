# Boundary estimates for every terminal power of magnitude at least thirty-two

Research proof, 2 November 2026. The crossing power is fixed before the
level tends to infinity. This note treats all signed powers $|n|\ge32$
with one argument. It uses the exact complete-meridian trace and the
already proved edge expansion on a fixed neighborhood of the complete
boundary. The frozen manuscripts are unchanged.

## 1. Statement and notation

Use the original terminal polynomial

\[
 H_{n,N}(u)=\sum_{k=0}^{N-1}\phi(R^n e_k)e_k(-2\cos u)
\]

defined in [the finite-transform note](research_terminal_powers_qbinomial.md).
Let $q=e^{\pi i/N}$, $d=N-1$, and $C_{N,n}=q^{nd^2/4}$.
The edge action is normalized by

\[
 \psi(0,0)=M_\infty=\frac{4G}{\pi},\qquad
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                       (\tan(t/2)\cos(u/2)),
\]

where $G$ is Catalan's constant. For $n>0$, let $t_n(u)$ be the
selected solution of

\[
 \psi_t(t,u)+\frac{in}{2\pi}t=i.
\]

Define

\[
 S_n(u)=\psi(t_n(u),u)+\frac{in}{4\pi}t_n(u)^2-it_n(u),
 \qquad M_n=\Re S_n(0).
\]

**Theorem.** For every fixed integer $n\ge32$, there is a complex disk
about $u=0$ on which

\[
 H_{n,N}(u)=C_{N,n}A_n(u)e^{NS_n(u)}(1+O_n(N^{-1})),        \tag{1}
\]

uniformly through all sufficiently large integer levels. The functions
$A_n,S_n$ are holomorphic and $A_n$ is nonzero after reducing the disk.
The normalized error is holomorphic, and its fixed derivatives satisfy
the same order on smaller disks. There are positive constants
$c_n,B_n,b_n,C_n$ and a finite $a_n$, independent of $N$, such that

\[
 |H_{n,N}(u+iv)|\le C_n N^{a_n}
       e^{N\{M_n-c_n(1-\cos u)+B_nv^2\}},
 \qquad |u|\le\pi,\quad |v|\le b_n.                       \tag{2}
\]

For negative powers, conjugate all coefficient functions and the exact
scalar $C_{N,n}$ as in the finite-transform note. This proves the same
statement for $n\le-32$. Constants in this theorem may depend on the
fixed power; no simultaneous limit in $n$ and $N$ is asserted.

## 2. Position and action of the selected saddle

Write $t_n(0)=2a-2ib$ with $a,b>0$. The
[stationary-geometry proof](research_terminal_powers_three_and_above.md)
gives

\[
 \sin a=\cosh b\tanh(nb),\qquad
 na+\arctan\frac{\sinh b}{\cos a}=\pi.
\]

In particular,

\[
 a<\frac\pi n,\qquad
 b\le\frac{\operatorname{artanh}(\sin(\pi/n))}{n}
      \le\frac{\pi\sec(\pi/32)}{n^2}\quad(n\ge32).       \tag{3}
\]

The last inequality follows by integrating
$(\operatorname{artanh}(\sin x))'=\sec x$.
Thus $\Re t_n<\pi/16<0.197$ and
$h_n=-\Im t_n=2b<0.0062$. Set $a_0=6/25=0.24$.
The rectangle $|\Re t|\le a_0$, $|\Im t|\le h_n$ lies strictly
inside $|t|<1/4$, with the selected saddle in its interior.

Allowing $n$ to vary over the real interval $[32,\infty)$ is legitimate
in these stationary equations. The solution is unique and nondegenerate.
Stationarity and (3) give

\[
 \frac{dM_n}{dn}=\frac{2ab}{\pi}
       \le\frac{2\pi\sec(\pi/32)}{n^3},
 \qquad M_n\longrightarrow M_\infty.
\]

Integration therefore proves

\[
 0<M_\infty-M_n\le\frac{\pi\sec(\pi/32)}{n^2}.          \tag{4}
\]

On the real axis,

\[
 M_\infty-\psi(a_0,0)
  =\frac1\pi\int_0^{a_0}\operatorname{arsinh}(\tan(t/2))\,dt
  \ge\frac{a_0^2}{4\pi}.
\]

Here $\operatorname{arsinh}(\tan s)\ge s$ follows from its derivative
$\sec s\ge1$. The elementary bounds
$\pi<22/7$ and $\sec(\pi/32)<101/100$ show that
$\pi\sec(\pi/32)/32^2<a_0^2/(4\pi)$. Consequently

\[
 \psi(a_0,0)<M_n,\qquad
 M_\infty-\pi/100<M_n.                                  \tag{5}
\]

The second inequality follows directly from (4).

## 3. Removing real angular and wire tails

Retain the original wire indices with $k/N\in I=[1/5,3/10]$.
The Hermite-norm estimate in
[the finite-source proof](../papers/circle-tree-volume/finite-bounds.tex)
shows that all omitted indices together contribute at most

\[
 C_nN^A e^{N(M_\infty-\pi/100)}                          \tag{6}
\]

to $H_{n,N}(u)$, uniformly for real $u$. Indeed the low-index rate is
$2g(k/N)$, where $g(x)=J(2x)-4J(x)$, and
$g''(x)\le-4\pi$ gives a loss at least $\pi/100$ outside $I$.
High indices have only polynomial Hermite and interval norms. This
estimate includes first normal derivatives and the original fixed
power $R^n$.

We also need a real angular bound at the smaller cutoff $a_0$.
The real summand rate is the function $A(x,r)$ in
[the real-angle tail proof](research_terminal_real_angle_tail.md), with
$r=(\pi-|t|)/(2\pi)$. In its region $x\le r$, its maximum is
$\psi(|t|,0)$, which decreases as $|t|$ increases. In the other region,
monotonicity in $r$ gives

\[
 A(x,r)\le H(x):=2J(2x)-6J(x),\qquad 0\le x\le1/2.
\]

For completeness, this last rate is uniformly less than one. Its
second derivative is

\[
 H''(x)=-4\pi\tan(\pi x)-2\pi\cot(\pi x)\le-4\pi.
\]

At $x=1/4$, $H=3G/\pi$ and $H'=\log2$. The quadratic tangent bound
therefore gives

\[
 H(x)\le\frac{3G}{\pi}+\frac{(\log2)^2}{8\pi}<1.        \tag{7}
\]

For the last comparison, $G<15/16$, $\log2<1$, and $\pi>3$ suffice.
On the other hand, $G>8/9$ and $\pi<22/7$, together with
$\operatorname{arsinh}(\tan(t/2))\le(t/2)\sec(a_0/2)$ for
$0\le t\le a_0$, give $\psi(a_0,0)>1$.
Thus the entire real outer region $|t|\ge a_0$ has rate at most
$\psi(a_0,0)$, even where a cosine factor has changed sign.

This is a summandwise estimate. It applies to the retained kernel

\[
 K_{N,I}(t,u)=\sum_{k/N\in I}e_k(-2\cos t)e_k(-2\cos u)
\]

as well as to the full kernel, uniformly in real $u$. Use the polynomial
interval bound $|e_k(-2\cos u)|\le CN^A e^{Ng(k/N)}$ for its second
factor. Polynomial differentiation on the interval
$[-2\cos a_0,2]$ gives the same rate for the first normal derivative.
Therefore the original derivative trace at outer angular nodes has
rate at most $\psi(a_0,0)<M_n$.

Choose the angular midpoint cutoff $a_N=a_0+O(N^{-1})$ with $a_N\ge a_0$.
The discarded nodes then satisfy the bound just proved. For all large
$N$, the thin rectangle with real endpoints $\pm a_N$ is still within
$|t|<1/4$.

## 4. The retained edge kernel on the whole lower contour

The original [edge expansion](../papers/circle-tree-volume/edge-packet.tex)
is uniform and holomorphic for $|t|,|u|\le1/4$:

\[
 K_{N,I}(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
                                                               \tag{8}
\]

with $a_e$ nonzero. The statement concerns precisely the retained
kernel above. It already estimates its exact wire-lattice corrections.

We record a weighted version of its upper bound, needed for all real
parent angles:

\[
 |K_{N,I}(t,u)|\le CN^A
   e^{N\{\Re\psi(t,0)-c(1-\cos u)\}},
 \qquad |t|\le1/4,\quad |u|\le\pi.                       \tag{9}
\]

To justify this extension, use the same exact wire contours as in the
edge proof with the second parent parameter fixed at zero. On each
main, correction, and endpoint piece, replace its second factor
$B_N(x,0)$ by $B_N(x,u)$. The uniform exact factorial bound and
Lemma 2 of [the boundary-decay proof](research_uniform_factorial_and_boundary_decay.md)
give an additional loss at least $c(1-\cos u)$ on all those pieces.
Their real wire coordinates remain in a fixed compact subinterval
of $(0,1/2)$ and their heights stay bounded. The same loss applies
to the translated Gaussian segment. All other estimates in the
edge proof are unchanged. This proves (9) for the complete retained
wire sum; it is not an estimate obtained by taking absolute values
of its real summands.

[The weighted edge proof](research_weighted_edge_contour_bound.md)
supplies the detailed contour bounds for this step, with angular
constant $c=1/20$ on the stated domain.

## 5. The exact trace and its unique saddle

Apply the midpoint-cutoff formula in
[the exact trace note](research_exact_complete_trace_contour.md)
with endpoint $a_N$ and depth $h_n=-\Im t_n(0)>0$.
Its lower horizontal integrand has rational kernel

\[
 W_N(t)=e^{-iNt}(1+O(e^{-Nh_n})),
\]

uniformly on that horizontal segment. This formula sums all higher
positive charges, with their original coefficients.

On the lower segment write $t=r-ih_n$. Its unit-charge phase is

\[
 F_n(t)=\psi(t,0)+\frac{in}{4\pi}t^2-it.
\]

Since

\[
 F_n''(t)=\frac{-\sec(t/2)+in}{2\pi},
 \qquad \Re F_n''(t)<0\quad(|\Re t|<\pi),                \tag{10}
\]

the real phase is strictly concave on the entire horizontal segment.
It has its unique maximum $M_n$ at the selected saddle. There is a
fixed gap outside any sufficiently small neighborhood of that point.
Equations (8)--(9) and the exact rational-kernel bound control all
nonunit charges below this same contribution.

The vertical current must also be estimated. Fold its upper half to
the negative real endpoint by oddness of the function $g$ in the trace
formula. At either lower endpoint $t=\pm a_N-iy$, $0\le y\le h_n$,
the reciprocal hyperbolic-cosine kernel contributes at most $e^{-Ny}$.
Thus its rate is bounded by $\Re F_n(\pm a_N-iy)$, using (8).
As a function of $y$, this real phase is convex, by (10). At $y=0$
it equals $\psi(a_N,0)\le\psi(a_0,0)<M_n$. At $y=h_n$ it is
strictly below $M_n$ by horizontal strict concavity. Convexity bounds
every intermediate point by the larger of these two endpoint values.
The entire exact vertical current therefore has a strict gap.

The same bounds persist for a small complex parent disk. The selected
saddle and all amplitudes continue holomorphically, while the compact
endpoint and exterior gaps remain strict. Ordinary uniform Gaussian
integration now proves (1). With the square roots inherited from
the edge Gaussian and continued near $u=0$, the coefficient is

\[
 A_n(u)=i\sqrt{\frac2\pi}\,
 \frac{a_e(t_n(u),u)\sin t_n(u)}
 {\sqrt{-\psi_{tt}(t_n(u),u)-in/(2\pi)}}.                 \tag{11}
\]

It is nonzero: the edge amplitude is nonzero, the Hessian has negative
real part, and $0<\Re t_n(0)<\pi$ with $\Im t_n(0)<0$ excludes
$\sin t_n(0)=0$. The exact scalar $C_{N,n}$ has not been approximated.
The powers of $N$ cancel: the trace gives $N^2$, the edge gives
$N^{-3/2}$, and its one-dimensional Gaussian gives $N^{-1/2}$.

## 6. The full boundary estimate

Equation (9) inserts a uniform real-parent angular loss into both
the lower horizontal integral and the endpoint current. The omitted
wire and angular terms have rates strictly below $M_n$ independently
of the real parent angle. Decrease the angular constant if necessary
so that those fixed losses also imply a bound of the form
$M_n-c_n(1-\cos u)$. This proves (2) first for $v=0$.

Near $u=0$, the holomorphic expansion (1) supplies the quadratic
complex-strip estimate. Indeed

\[
 S_n''(0)=-\frac{\cos(t_n(0)/2)}{2\pi},\qquad
 \Re S_n''(0)<0.
\]

Taylor's formula and Young's inequality absorb its mixed real-imaginary
quadratic term. Away from a small neighborhood of zero, apply the
polynomial Bernstein--Walsh bound on a slightly larger real spectral
interval that still has a fixed angular loss. A sufficiently thin
complex neighborhood preserves half that loss. Combining the two
regions gives (2), exactly as in the
[two-crossing global bound](research_two_crossing_terminal_filling.md).

The proof establishes complete boundary packets for all fixed
$|n|\ge32$. The smaller powers are treated separately in
[the combined terminal-filling theorem](research_verified_terminal_fillings_and_long_remainder.md).
Stability when adjacent vertices are filled with short powers remains
a separate requirement.
