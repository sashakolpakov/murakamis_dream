# One-sided wire summation along the filling contour

Research note, 2 November 2026. This gives exact nested contour
identities. It also proves that the initial \(O(N^{-1})\) portion
of the positive-cutoff filling current is exponentially smaller
than the selected saddle, using the real outer-angle estimate.
No bound on the remaining coupled faces or Fourier modes is
asserted.

The exact interpolation and its holomorphy are established in
[the coupled residue note](research_terminal_coupled_residue_identity.md).
The starting real estimate is
[the terminal real-angle tail theorem](research_terminal_real_angle_tail.md).

## 1. An upper-contour formula with all corrections retained

Let \(a,b\) be half-grid points:

\[
Na,Nb\in\mathbb Z+\frac12,\qquad a<b.
\]

Suppose \(f\) is holomorphic on a neighborhood of
\([a,b]+i[-h,h]\), where \(h>0\). The kernel

\[
\mathscr L_N(z)
=\pi N\cot(\pi Nz)-i\pi N
=\frac{2\pi iN}{e^{2\pi iNz}-1}
                                                        \tag{1}
\]

has residue one at each wire node \(k/N\). On the upper side it has
a constant term; on the lower side it does not. Put

\[
E_+(r,h)=e^{2\pi iN(r+ih)},\qquad
E_-(r,h)=e^{-2\pi iN(r-ih)}.
\]

Both have modulus \(e^{-2\pi Nh}\). The exact formula is

\[
\boxed{
\begin{aligned}
\sum_{a<k/N<b}f(k/N)
={}&N\int_a^b f(r+ih)\,dr\\
&+N\int_a^b f(r+ih)
       \frac{E_+(r,h)}{1-E_+(r,h)}\,dr\\
&+N\int_a^b f(r-ih)
       \frac{E_-(r,h)}{1-E_-(r,h)}\,dr\\
&-iN\int_{-h}^{h}
 \frac{f(b+iy)-f(a+iy)}{1+e^{-2\pi Ny}}\,dy.
\end{aligned}}                                           \tag{2}
\]

**Proof.** Integrate \(f(z)\mathscr L_N(z)/(2\pi i)\)
counterclockwise around the rectangle. The bottom side runs left to
right, and the top side runs right to left. On the top,

\[
\frac{\mathscr L_N(z)}{2\pi i}
=-\frac{N}{1-e^{2\pi iNz}},
\]

so its reversed orientation gives the first two lines of (2).
On the bottom,

\[
\frac{\mathscr L_N(z)}{2\pi i}
=N\frac{e^{-2\pi iNz}}{1-e^{-2\pi iNz}},
\]

giving the third line. On either half-grid vertical side,
\(e^{2\pi iN(a+iy)}=e^{2\pi iN(b+iy)}=-e^{-2\pi Ny}\).
Since \(dz=i\,dy\), the difference of the right and left sides is
the last line. The residue theorem now gives (2). \(\square\)

The first line has coefficient \(N\), not \(N/2\). It is the only
constant horizontal contribution. The other three lines are exact
parts of the identity, not error notation.

The two horizontal correction kernels have convergent expansions

\[
\frac{E_\pm}{1-E_\pm}=\sum_{p=1}^{\infty}E_\pm^p
\quad(h>0).                                             \tag{3}
\]

They can instead be retained as rational functions, or truncated
exactly using

\[
\frac{E}{1-E}
=\sum_{p=1}^{P}E^p+\frac{E^{P+1}}{1-E}.
                                                        \tag{4}
\]

No mode in (3) has been discarded in (2).

The useful pointwise bounds on the weights are

\[
\left|\frac{E_\pm}{1-E_\pm}\right|
\leq\frac{e^{-2\pi Nh}}{1-e^{-2\pi Nh}},                  \tag{5}
\]

\[
0<\frac1{1+e^{-2\pi Ny}}
\leq
\begin{cases}
1,&y\geq0,\\
e^{-2\pi N|y|},&y\leq0.
\end{cases}                                             \tag{6}
\]

Thus a lower horizontal wire correction carries a loss
\(2\pi h\) in its exponential rate. The same is true of the upper
horizontal correction. The lower portions of the two endpoint
currents have the varying loss \(2\pi|y|\); the upper portions have
no such factor. A bound on the upper endpoints cannot be inferred
from the lower correction weights.

## 2. Apply the formula pointwise on the filling current

Let the positive-cutoff filling path be

\[
t_s=T_N+\delta_\sigma-i h_t s,\qquad
\delta_\sigma=\frac{2\pi\sigma}{N},\qquad 0\leq s\leq1.
\]

Here \(T_N=T+O(N^{-1})\), with \(T=2\pi/3\), is the half-grid
cutoff for the filling variable. Let \(g_N(x,t)\) be holomorphic
on the required wire rectangles, and let \(w_N(s)\) denote the
entire remaining filling-current weight, including its oriented
differential if that differential is parametrized by \(s\).
Consider

\[
\mathcal C_N
=\int_0^1 w_N(s)
      \sum_{a<k/N<b}g_N(k/N,t_s)\,ds.
                                                        \tag{7}
\]

The weight may include the original integer crossing chirp, the
sine factor, and the exact rational trace kernel. The identity
below does not replace any of them by its leading asymptotic term.

For \(s>0\), choose

\[
h_s=h_xs,\qquad h_x>0.
\]

Formula (2), with \(t=t_s\) held fixed during the wire contour,
gives the exact sum of four quantities:

\[
\sum_{a<k/N<b}g_N(k/N,t_s)
=\mathcal M_N(s)+\mathcal U_N(s)
 +\mathcal L_N(s)+\mathcal E_N(s),                       \tag{8}
\]

where

\[
\mathcal M_N(s)=N\int_a^b g_N(r+i h_xs,t_s)\,dr,
\]

\[
\mathcal U_N(s)=N\int_a^b
 g_N(r+i h_xs,t_s)
 \frac{e^{2\pi iN(r+i h_xs)}}
      {1-e^{2\pi iN(r+i h_xs)}}\,dr,
\]

\[
\mathcal L_N(s)=N\int_a^b
 g_N(r-i h_xs,t_s)
 \frac{e^{-2\pi iN(r-i h_xs)}}
      {1-e^{-2\pi iN(r-i h_xs)}}\,dr,
\]

\[
\mathcal E_N(s)=-iN\int_{-h_xs}^{h_xs}
\frac{g_N(b+iy,t_s)-g_N(a+iy,t_s)}
     {1+e^{-2\pi Ny}}\,dy.
                                                        \tag{9}
\]

The main wire integral therefore has precisely the simultaneous
heights

\[
x=r+i h_xs,\qquad t=T_N+\delta_\sigma-i h_ts.
\]

No two-dimensional homotopy theorem is needed to obtain this
particular face: it follows from a one-variable residue identity
for every fixed value of \(s\), followed by integration in \(s\).
All holomorphy conditions concern the full rectangles
\([a,b]+i[-h_xs,h_xs]\) at the fixed value \(t_s\).

The endpoint terms require a larger set of points than just the
diagonal corners of the main face. They contain

\[
x=a+iy\ \hbox{or}\ b+iy,\qquad
|y|\leq h_xs,\qquad
t=T_N+\delta_\sigma-i h_ts.
                                                        \tag{10}
\]

Any proposed endpoint bound must hold on this full triangular
parameter region, with the weights (6).

## 3. Separate the initial \(N^{-1}\) collar

Individual absolute bounds in (5) degenerate as \(s\to0\). The
identity itself has no singularity there, but separately estimating
its pieces by a multiple of \(1/s\) would lose that cancellation.
A direct remedy is to leave the original wire sum untouched for
\(0\leq s\leq N^{-1}\). Exactly,

\[
\begin{aligned}
\mathcal C_N
={}&
\int_0^{1/N}w_N(s)
          \sum_{a<k/N<b}g_N(k/N,t_s)\,ds\\
&+\int_{1/N}^1 w_N(s)
  \{\mathcal M_N(s)+\mathcal U_N(s)
     +\mathcal L_N(s)+\mathcal E_N(s)\}\,ds.
                                                        \tag{11}
\end{aligned}
\]

On the second interval,

\[
1-e^{-2\pi Nh_xs}\geq1-e^{-2\pi h_x}>0.
\]

Both horizontal correction weights are consequently bounded by

\[
\frac{e^{-2\pi Nh_xs}}{1-e^{-2\pi h_x}}.                 \tag{12}
\]

Formula (11) avoids moving an infinite Fourier series onto the
wire lattice. It also avoids imposing a positive lower height at
\(s=0\) merely to regularize a term that was already finite before
the contour decomposition.

On the lower horizontal filling contour itself, \(t\) already has
the fixed depth \(-h_t\). One applies (2) directly with the fixed
wire height \(h_x\). The main contribution has upper wire height
\(h_x\); its two horizontal corrections have the fixed exponential
weight in (5); and its endpoint currents have precisely the
fixed-\(t\) weights in the final line of (2).

## 4. The initial collar is below the selected action

For the actual complete-parent source, use the full wire sum

\[
K_N(t,0)=\sum_{k=0}^{N-1}
 e_k(-2\cos t)e_k(-2).
\]

The real-angle theorem proves, with \(T=2\pi/3\),

\[
\sup_{T\leq t\leq\pi}|K_N(t,0)|
\leq C N^A e^{N\psi(T,0)},
\qquad
\psi(T,0)<\frac45<\frac56\leq M_n
\quad(|n|\geq3).                                       \tag{13}
\]

Write \(K_N(t,0)=P_N(-2\cos t)\). Its degree is at most \(N-1\).
On the real interval

\[
I_z=[-2\cos T,2]=[1,2],
\]

the bound (13) therefore controls \(P_N\).

An elementary polynomial continuation estimate suffices near the
endpoint. If a polynomial \(P\) has degree at most \(d\) and
\(\sup_{[c-a,c+a]}|P|\leq B\), then

\[
|P(z)|\leq B|\zeta(z)|^d,\qquad
\frac{z-c}{a}=\frac{\zeta+\zeta^{-1}}2,\quad |\zeta|\geq1.
                                                        \tag{14}
\]

To prove (14), the function
\(\zeta^dP(c+a(\zeta+\zeta^{-1})/2)\) is a polynomial of degree
at most \(2d\), bounded by \(B\) on the unit circle. The maximum
principle applied outside that circle after division by
\(\zeta^{2d}\) gives (14). This is the interval form of the
Bernstein--Walsh inequality. At an endpoint, the quadratic equation
for \(\zeta\) gives

\[
\log|\zeta(z)|=O\!\left(
          \operatorname{dist}(z,I_z)^{1/2}\right).
\]

For \(|\sigma|\leq\rho<1/2\) and \(0\leq s\leq N^{-1}\),

\[
t_s=T+O(N^{-1}),\qquad
-2\cos t_s=1+O(N^{-1}),
\]

uniformly for fixed \(h_t,\rho\). Applying (14) to (13) gives

\[
|K_N(t_s,0)|
\leq C N^A
       \exp\{N\psi(T,0)+C_1\sqrt N\}.                  \tag{15}
\]

The additional cost is subexponential. It does not require a
factorial estimate at moving zeros or a complex continuation of
each individual wire summand.

For the actual filling current, all remaining factors have at
most polynomial growth on this collar, at each fixed integer
\(n\), when the meridian parameter is first restricted to a
circle \(|\sigma|=\rho<1/2\). The crossing chirp has modulus
\(e^{O_n(1)}\), since \(\Im t_s=O(N^{-1})\). The sine factor is
bounded. The trace kernel is \(O(N)\) on the half-grid vertical
side: its exponential quotient has the form
\(1/(1+e^{\pm Nh_ts})\), possibly with the harmless constant
term of the chosen residue kernel. Also
\(\sin(2\pi\sigma)\) is bounded away from zero on that circle.

Thus the original full-source current restricted to
\(0\leq s\leq N^{-1}\) is bounded by

\[
C_n N^{A_n}\exp\{N\psi(T,0)+C_1\sqrt N\}.
                                                        \tag{16}
\]

For sufficiently large \(N\), this is below
\(\exp\{N(M_n-\gamma)\}\) for some fixed \(\gamma>0\).
One may take any \(\gamma<1/30\) after absorbing the
subexponential and polynomial factors. The holomorphic,
odd-projected trace expression has the same bound at
\(\sigma=0\) by the maximum principle, with its Hermite
derivatives retained.

This collar argument is for the full wire polynomial. If a proof
first divides the wire sum into subsets, it must either retain
their combined collar as above or separately justify estimates
for the restricted polynomials. A bound for the complete sum
cannot be assigned to arbitrary partial sums.

## 5. Remaining estimates in the nested construction

The nested equalities now reduce the current away from its initial
collar to four explicit pieces:

1. The coupled main integral \(\mathcal M_N\).
2. The upper correction \(\mathcal U_N\), with (12).
3. The lower correction \(\mathcal L_N\), with (12).
4. The two endpoint differences \(\mathcal E_N\) on (10), with
   the asymmetric weights (6).

For the lower horizontal filling contour, the corresponding
pieces are given by the fixed-height instance of (2). These are
exact reductions; each remaining exponential comparison must
still be proved on its stated domain. In particular, smallness
of the coupled main face does not automatically control the
lower wire correction or the full endpoint region.
