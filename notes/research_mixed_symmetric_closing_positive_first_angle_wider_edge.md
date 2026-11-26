# The wider outgoing edge with every positive first angle

Private finite-source deduction, 9 November 2026. This extends the
first real angle in the adopted wider-right edge envelope down to
any fixed positive cutoff. The outgoing real angle still extends
to \(2\pi/3\), with height \(7/10\). It is a bound for the exact
shortened edge, not an estimate of the whole inner trace.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, or frozen-source edit is used.

## 1. Exact source and domain

Fix \(0<a_L<\pi/2\), and retain
\[
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}
                  e_j(-2\cos t)e_j(-2\cos u).
 \tag{1}
\]
The independent parameter set is
\[
 \begin{gathered}
 t=a-iH,\quad a_L\le a\le2\pi/3,\quad1/10\le H\le1,\\
 u=\beta-iK,\quad0\le\beta\le2\pi/3,\quad0\le K\le7/10.
 \end{gathered}
 \tag{2}
\]
Use the original zero-charge critical value \(\psi(t,u)\), with
the same complete-edge constant as in the
[wider-right theorem](research_mixed_symmetric_closing_wider_right_edge_envelope.md).
Its continuation over (2) is verified below.

**Theorem.** For each fixed \(\tau>0\), there is \(C_{\tau,a_L}\)
such that, uniformly on (2) through both level parities,
\[
 |K_N^<(t,u)|\le C_{\tau,a_L}
       \exp N\left[
          \max\left\{\Re\psi(t,u),\frac{H+K}{2}\right\}+\tau
       \right]
 \tag{3}
\]
for all sufficiently large \(N\).

All rows in (1), both physical endpoint groups, the two complete
Fourier corrections, and the original external caps remain.
No nonzero coefficient or relative edge packet is asserted.

## 2. Cut estimates on the larger first-angle interval

Put \(F(y)=b(y,t)+b(y,u)\). Its exact force is
\[
 e^{F_y}
 =\frac{(\cos2\pi y+\cos t)(\cos2\pi y+\cos u)}
             {(1-\cos2\pi y)^2}.
 \tag{4}
\]
Every cut estimate in Sections 2--3 of the wider-right theorem
used the own real angle only through
\[
                  d=\cos(\text{own angle})\ge-1/2.
 \tag{5}
\]
The comparison of the own squared numerator with its value at
\(d=-1/2\) holds for the entire range \(d\le q\le1\), including
\(d>0\). The other leg enters only through
\[
 |\cos(\text{other leg})|\le\mu,\quad
 \Re\cos(\text{other leg})\ge-\mu/2,\quad
 \Im\cos(\text{other leg})\ge0.
 \tag{6}
\]
For the incoming cut take
\(\mu=13/10\), \(1\le\cosh H<8/5\); for the outgoing cut
take \(\mu=8/5\), \(1\le\cosh K<13/10\).
All these hypotheses remain true on (2). In particular neither
of the cleared polynomial estimates used \(a\ge\pi/2\).

Thus the four literal guards proved there remain
\[
 \begin{array}{c|cc}
 &q\ge0&q\le0\\ \hline
 \text{incoming cut}
   &|e^{F_y}|^2<499/500&|e^{F_y}|\le117/(80\sqrt3)<1\\
 \text{outgoing cut}
   &|e^{F_y}|^2<1999/2000&|e^{F_y}|\le9/10<1.
 \end{array}
 \tag{7}
\]
An empty negative-coordinate part requires no separate estimate.
The guards include starting zeros, cut intersections and all
one-sided limiting values. Hence the continuous original
reciprocal-factorial envelope has a strict horizontal descent
on every cut. The original reflected logarithms, not a newly
chosen logarithm of (4), are used.

## 3. Root and charge on the enlarged domain

Set
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D_0=A+B-AB,\quad W=AB/D_0.
 \tag{8}
\]
The only bound in the wider-right theorem that needs changing is
the upper bound for \(|A|\). The valid replacement is
\[
 \Re A>1/10,\quad |A|<13/10,\quad |1-A|<21/20,
 \quad \Im A>0,\quad \Re(1/A)>5/32.
 \tag{9}
\]
Indeed, with \(C=\cosh H<8/5\) and \(d=\cos a\in[-1/2,1]\),
\[
 \Re A=(1+Cd)/2,\quad |A|=(C+d)/2,\quad
 |1-A|=(C-d)/2,\quad
 \Re(1/A)=\frac{2(1+Cd)}{(C+d)^2}.
 \tag{10}
\]
The derivative of the last expression in \(d\) has the sign of
\(C^2-Cd-2\). An interior critical point is therefore a maximum.
At \(d=1\) its value is \(2/(C+1)>10/13\). At \(d=-1/2\)
it is \((2-C)/(C-1/2)^2>40/121\): this expression decreases
on \(1\le C\le8/5\). Both lower bounds exceed \(5/32\).
Strict positivity of \(\Im A\) is uniform for fixed \(a_L\).

The outgoing estimates are unchanged:
\[
 \Re B>7/40,\quad |B|<23/20,\quad |1-B|<9/10,\quad
 \Im B\ge0,\quad \Re(1/B)>20/23.
 \tag{11}
\]
Consequently
\[
 \Re D_0>11/200,\quad
 \Re(1/W)>19/736,\quad \Im(1/W)<0.
 \tag{12}
\]
For fixed \(a_L\), \(W\) stays in a compact subset of the upper
right quadrant. The principal expressions
\[
 y_*=\pi^{-1}\arctan\sqrt W,\qquad
 -F_{yy}(y_*)=\frac{2\pi D_0(1+W)^2}{W^{3/2}}
 \tag{13}
\]
therefore give a simple finite critical point in the upper
half-strip. The original algebraic identity
\[
 e^{F_y}-1
  =-\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},
                  \qquad z_y=\tan\pi y,
 \tag{14}
\]
gives uniqueness there.

Calibration can be made without extending an old theorem by
assertion. Start at \(a=\pi/2,u=0\), where the adopted theorem
has \(F_y(y_*)=0\) and the original critical value \(\psi\).
Move \(a\) along its real interval to the desired value, holding
\(H\) fixed and \(u=0\), and then move \(u\) along its straight
segment from zero. The entire path satisfies (7),(9)--(12).
A force-one point cannot meet a cut, a numerator zero or the
half-strip boundary. The original continuous logarithmic
derivative belongs to \(2\pi i\mathbb Z\), so it remains zero.
Continuing the original primitive along the same paths gives
\[
                 F_y(y_*)=0,\qquad F(y_*)=\psi(t,u).
 \tag{15}
\]
There is no new additive constant or charge.

## 4. Complete contour and finite interpolation

Write \(\mathcal V=\mathfrak b(\,\cdot\,,t)+
\mathfrak b(\,\cdot\,,u)\), the original zero-safe envelope.
Its endpoint values remain \(0\) and \(e=(H+K)/2\).
It is continuous and subharmonic, including the upward
\(2\pi\) jumps across cuts and the vanishing
\(O(\rho|\log\rho|)\) starting-zero flux.

The original one-leg force on the real wire has numerator
\(\cos2\pi x+\cos(\theta-ih)\). For \(0<\theta<\pi,h>0\)
its original argument lies in \((0,\pi)\). This follows at
\(x=0\) from \(2\arg\cos((\theta-ih)/2)\), and then by
continuation in \(x\) without a real-axis crossing. The
incoming leg in (2) is always strict. Hence there is no
bottom local minimum; at real outgoing cuts retain (7)
and the one-sided reflection limits instead. At \(\beta=0\)
the outgoing argument is zero and the incoming one suffices.

The original side identities in the
[vertical-envelope theorem, Section 3](research_mixed_next_selected_right_edge_vertical_upper_envelope.md)
hold for all real leg angles \(0\le\theta<\pi\). The left
trace increases from zero. The right trace decreases until
the smaller cut height and then increases, with the stated
zero-angle limiting interpretation. Each strict side sublevel
is connected or empty. The upper asymptotic remains
\[
 \mathcal V(x+iv)
   =2\pi v-D_*+o(1),\qquad
                   D_*=\frac{aH+\beta K}{2\pi}.
 \tag{16}
\]
Together with (7),(13), these are exactly the hypotheses
of the adopted component/Jordan construction. Its descending
germs reach different vertical sides. Joining to the real
endpoints costs at most \(\max\{\Re\psi,e\}+\epsilon\).
Fixed small collars and a finite compact parameter cover
give uniform lengths and heights.

Use the identical interpolation
\[
 \begin{split}
 B_N(y,z)&=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\\
 T_N(y)&=B_N(y,t)B_N(y,u).
 \end{split}
 \tag{17}
\]
Its values at \(j/N\) are exactly the rows of (1).
The shifted real arguments still lie in \([-1/3,5/6]\);
decreasing \(a\) does not enlarge this interval. The original
zero-safe factorial bounds are therefore unchanged.

Both aliases retain their complete rational denominators.
Their side rates are at most \(D_*\) and \(e\), and
\[
                 e-D_*\ge(H+K)/6\ge1/60.
 \tag{18}
\]
At wire height two the same complete reflected dilogarithm
remainder is below \(1/600\). Thus both deep alias rates
are below \(e-3/200\). The original midpoint caps have
denominator \(-1-e^{-2\pi Nv}\) and reciprocal modulus at
most one.

More explicitly, with the original midpoint columns
\(\alpha_N,\gamma_N\), fixed collar height \(h_c>0\) and
\(\zeta=e^{2\pi iNy}\), the exact decomposition is
\[
 \begin{split}
 K_N^<={}&N\int_{\Gamma_+}\frac{T_N}{1-\zeta}\,dy
       +N\int_{\Gamma_-}\frac{T_N}{\zeta-1}\,dy+C_N+E_N,\\
 C_N={}&N\int_{\gamma_N-ih_c}^{\gamma_N+ih_c}
                      \frac{T_N}{\zeta-1}\,dy
       -N\int_{\alpha_N-ih_c}^{\alpha_N+ih_c}
                      \frac{T_N}{\zeta-1}\,dy,\\
 E_N={}&\sum_{j=0}^{\lfloor N\alpha\rfloor}T_N(j/N)
        +\sum_{j=\lceil N\gamma\rceil}^{U_N}T_N(j/N).
 \end{split}
 \tag{19}
\]
Here \(\Gamma_+\) and \(\Gamma_-\) have their original
left-to-right orientations. Splitting the upper denominator
produces the whole unweighted term. Its endpoint additions
are
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy+
 N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy,
 \tag{20}
\]
with these signs. The remaining upper and lower corrections
use the depth-two paths and full \(2\pi N|\Im y|\) penalty.
Every physical endpoint row in \(E_N\) and every cap in
(19)--(20) is bounded using the same collars.
The resulting bound is a fixed polynomial in \(N\) times
\(\exp N(\max\{\Re\psi,e\}+\epsilon)\). Taking
\(\epsilon<\tau/2\) proves (3).

## 5. Scope

This theorem licenses the second edge on an entire positive
first-angle horizontal away from \(a=0\), at every height in
(2). It does not license a mixed-sign first height. In
particular, reflecting a negative first real angle changes
that sign and cannot be followed by a conjugation that
silently changes the outgoing parameter or the cubic
crossing.

An enlarged signed central contour still needs its own
source proof, including its center polynomial argument.
Even after that, the attached geometric and endpoint-sector
rates, the low/far inner currents, and the complete right
outer connector must be compared with the closing action.
No such comparison follows from (3).

## Frozen source bindings

- Wider-right exact edge and all four cut inequalities:
  46a3993146fa259ae70f7acbf861daa106b2b94f15ebb7bbdb92782126d21868.
- Original side limits and complete upper-envelope construction:
  2498045028562d23a06990b9175d9799177c0e2896c2d5eaf0e51d0d082c31d6.
- Subharmonic component/Jordan argument:
  b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542.
- Literal finite interpolation, orientations and external caps:
  1588e16cedaa06fd3f9e1d403cd642032ed5929e3e7741014994af5c51058b9d.
- Uniform zero-safe factorial estimates:
  4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
