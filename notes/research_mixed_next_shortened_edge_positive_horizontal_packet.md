# The shortened second edge on complete positive horizontal segments

Private written finite-source theorem, 8 November 2026. The complete
shortened-edge packet holds when the real first angle varies over any
fixed positive interval ending at \(\pi/2\), at its original actual
cubic height. The wire saddle need not remain in the first quarter.
Two strict-sublevel paths replace that restriction. A separate lower
rectangle pays the complete lower Fourier current.

All physical rows of the shortened edge, both exact Fourier
denominators, the external caps, and the original Gaussian
normalization are retained. No mathematical numerical evaluation or
change to a frozen source is used. This theorem does not extend the
first complete edge or estimate the complete inner trace.

## 1. Family, finite source, and statement

Keep the actual positive outer family and cubic branch:
\[
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},
 \qquad t_*(u)=a_*(u)-iH(u).
 \tag{1}
\]
The [cubic source](research_mixed_next_inner_three_cubic_continuation.md)
and [ordered-height proof](research_mixed_next_shortened_edge_upper_terminal_regions.md)
give uniformly
\[
             0<a_*(u)<\pi/2,\qquad 1/2<H(u)<1,\qquad H(u)>K .
 \tag{2}
\]
For any fixed \(0<a_L<\pi/2\), define
\[
 \mathcal S_L=
 \{(a-iH(u),u):u\in\mathcal U_+,\ a_L\le a\le\pi/2\}.
 \tag{3}
\]
The angular depth \(H(u)\) is held fixed along each segment.
Only its original starting point \(a=a_*(u)\) is asserted to
solve the coupled cubic equation.

The exact finite source is unchanged:
\[
 \begin{gathered}
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\quad
 c_\nu=2\cos((2\nu+1)\pi/N),\quad
 e_j(\xi)=S_j^{-2}\prod_{\nu<j}(c_\nu-\xi),\\
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^{<}(t,u)=\sum_{j=0}^{U_N}
                      e_j(-2\cos t)e_j(-2\cos u).
 \end{gathered}
 \tag{4}
\]
In particular the odd middle row is absent for exactly the
original [outer-annihilator reason](research_mixed_next_outer_exact_low_edge_reduction.md).

**Theorem.** There are fixed independent complex neighborhoods
\(\mathcal O'\), \(\mathcal O\) of \(\mathcal S_L\), with
\(\overline{\mathcal O'}\subset\mathcal O\), such that, uniformly
for all sufficiently large \(N\) at both parities,
\[
 K_N^{<}(t,u)
   =N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})).
 \tag{5}
\]
Here \(\psi\) is the original calibrated edge action. Put
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D_0=A+B-AB,\quad W=\frac{AB}{D_0}.
 \tag{6}
\]
The original saddle and coefficient are
\[
 y_*=\frac{\arctan\sqrt W}{\pi},\qquad
 a_e(t,u)=\frac{1}{4\sqrt{D_0}\,W^{1/4}}\ne0,
 \tag{7}
\]
with the principal powers continued on their indicated right
half-planes. Equivalently this is the original coefficient
\[
 a_e(t,u)=
 \frac{\sqrt{2\pi}}
 {4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*;t,u)}}.
 \tag{8}
\]
For every fixed \(r,s\ge0\),
\[
 \sup_{\mathcal O'}
 \left|\partial_t^r\partial_u^s
 \left\{N^{3/2}e^{-N\psi(t,u)}K_N^{<}(t,u)-a_e(t,u)\right\}\right|
                     \le C_{r,s}/N .
 \tag{9}
\]
No estimate of a further angular trace is asserted.

For the proof, if necessary replace \(a_L\) temporarily by
\[
 a_0=\min\{a_L,\tfrac12\min_{\mathcal U_+}a_*(u)\}>0.
 \tag{10}
\]
This larger compact segment family contains the complete actual
graph and is connected. We prove the statement on that family
and then restrict to (3).

## 2. The unique saddle and its original sheet

For \(t=a-iH\), put \(C=\cosh H<8/5\) and \(c=\cos a\in[0,1]\).
Then
\[
 \Re A=\frac{1+cC}{2}\ge\frac12,\quad
 \Im A=\frac{\sin a\sinh H}{2}>0,\quad
 |A|=\frac{C+c}{2}.
 \tag{11}
\]
We do not require \(|A|<1\). The exact identity
\[
 (1+cC)(1+C)-(C+c)^2
       =(1-c)(c+1+C-C^2)\ge0
 \tag{12}
\]
holds because \(1+C-C^2>1/25\) for \(1\le C<8/5\).
Consequently
\[
              \Re(1/A)\ge\frac{2}{1+C}>\frac{10}{13}.
 \tag{13}
\]
The unchanged outgoing guards give
\[
 \Re(1/B)>\frac{14}{15},\qquad \Im(1/B)\le0,\qquad B\ne0 .
 \tag{14}
\]
Thus
\[
 \Re(1/W)=\Re(1/A+1/B-1)>\frac{137}{195},
 \qquad \Im(1/W)<0 .
 \tag{15}
\]
The strict imaginary inequality is uniform on the compact family
in (10), since \(a\ge a_0>0\) and \(H>1/2\).
It follows that \(W\) stays in a compact subset of the first
quadrant. The specified \(y_*\) is in
\[
                  0<\Re y_*<1/2,\qquad \Im y_*>0 .
 \tag{16}
\]
Unlike the right-segment theorem, no assertion
\(\Re y_*<1/4\) or \(|W|<1\) is used.

The original regular or sidewise phase is
\[
 \begin{split}
 b(y,z)&=-J(1/2-y+z/(2\pi))
         -J(1/2-y-z/(2\pi))-2J(y),\\
 F(y;t,u)&=b(y,t)+b(y,u),\qquad
                       J'(w)=\Log(2\sin\pi w).
 \end{split}
 \tag{17}
\]
Its upper cuts for \(z=\theta-iA_0\) are exactly
\[
  y=x+iA_0/(2\pi),\qquad
                 1/2-\theta/(2\pi)\le x<1/2.
 \tag{18}
\]
The original upper envelope is continuous across them, but the
holomorphic phase is taken on their complement.

The force estimates from the
[upper terminal-region proof, Section 3](research_mixed_next_shortened_edge_upper_terminal_regions.md)
remain valid on the larger family, with one explicit change.
Now \(|\cos t|\le\cosh H<8/5\), while
\(|\cos u|<8/7\). The own-leg bound on a cut of angular depth
\(A_0\) is
\[
 \frac{|\cos(2\pi y)+\cos z|}{|1-\cos(2\pi y)|}
       \le\frac{\sqrt{2\cosh^2 A_0-1}}{1+\cosh A_0}.
 \tag{19}
\]
The other leg is at most \(\max(1,|\cos z'|)\), because the
two numerator vectors are in opposite closed quadrants.
Accordingly the full force on the \(u\) cut is at most
\[
       \frac{8\sqrt{79}}{75}<1
       \quad\left(\frac{5056}{5625}<1\right);
 \tag{20}
\]
on the \(t\) cut its squared modulus is less than
\[
                         \frac{6592}{8281}<1 .
 \tag{21}
\]
These include the initial zero by continuity. Empty cuts at
\(\theta=0\) create no additional case.

For \(z_y=\tan(\pi y)\), the exact algebraic critical equation is
\[
 e^{F_y}-1=
       -\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4}.
 \tag{22}
\]
The map \(y\mapsto z_y\) maps the open upper half-strip onto the
first quadrant. The factor \(z_y^2+1\) never vanishes there,
and the sole remaining root is \(z_y=\sqrt W\). Equations
(20)--(21) prevent that root, whose force has modulus one,
from lying on either cut (18), including a starting zero.
The compact selected saddle family therefore has a positive
distance from all these cuts and zeros.

For each fixed \(u\), continue \(a\) from \(a_*(u)\) to the
desired point of (10). Along this segment the selected saddle
does not cross a cut, and its original \(F_y\) is continuous.
By (22) it lies in \(2\pi i\mathbb Z\). It starts at the
adopted zero lift, so
\[
                         F_y(y_*;t,u)=0 .
 \tag{23}
\]
This proves the logarithmic charge, rather than only the
exponentiated equation. The critical value is the original
\(\psi\): the full-box closed primitive in
[the endpoint-gap theorem, Lemma 1](research_mixed_next_shortened_edge_endpoint_gap.md)
agrees with \(F(y_*)\) on the adopted graph neighborhood, and
analytic continuation along the connected segment family
preserves that equality. No additive constant is reset.

Differentiating (22) at the root gives
\[
 -F_{yy}(y_*)=
           \frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0 .
 \tag{24}
\]
Indeed
\[
 |1-A|<4/5,\qquad |1-B|<4/7,\qquad
                    \Re D_0>19/35 .
 \tag{25}
\]
These follow from
\(|\sin^2(t/2)|=(\cosh H-\cos a)/2\) and its outgoing analogue.
The principal powers in (7) are thus single-valued on a common
neighborhood. The identity
\(\sin^2(\pi y_*)=W/(1+W)\) reduces (8) to (7).
Its sign is the original one: at completeness it is \(1/4\),
and the unchanged original Gaussian root continues to the
adopted graph. For a direct check on that graph, write
\(\theta=\arg W\), \(\phi=\arg(1+W)\), and
\(\delta=\arg D_0\). There \(|W|<1\), so
\(0<\phi<\theta/2\), and
\[
 -5\pi/4<\delta+2\phi-3\theta/2<\pi/2.
\]
Since the adopted graph also has \(\Re(-F_{yy})>0\), this
argument must belong to \((-\pi/2,\pi/2)\). Thus the square
root used in (7)--(8) is exactly the original positive-real-part
Gaussian root there.
The powers in (7) then continue it throughout (10).

## 3. Two complete upper descent paths

Let
\[
             \mathcal V(y)=\mathfrak b(y,t)+\mathfrak b(y,u),
             \qquad m=\Re\psi(t,u).
 \tag{26}
\]
All the following are statements about the original sidewise
reciprocal-factorial upper envelope. The complete endpoint
theorem applies to our larger family and gives
\[
                    m>(H+K)/2+1/25>0 .
 \tag{27}
\]
Thus both real physical endpoint groups have a fixed strict gap.

We apply the rectangle lemma of
[the complete upper-continuation theorem, Lemma 1](research_mixed_next_shortened_edge_upper_continuation.md)
on \(0\le x\le1/2,\ 0\le v\le V\). Its hypotheses continue
to hold without a first-quarter restriction:

* The envelope is continuous and subharmonic. Across either
  cut (18), the derivative in upper wire height has the same
  positive jump \(2\pi\). The starting-zero flux is
  \(O(\epsilon|\log\epsilon|)\) and tends to zero.
* On a cut the horizontal derivative is at most the logarithm
  of the fixed constant less than one in (20)--(21). This is
  a strict descent direction, also at its starting zero.
* At regular points the envelope is harmonic and nonconstant.
  On the open bottom edge before a possible real outgoing cut,
  its inward derivative is negative: the \(t\)-leg force has
  strictly positive imaginary part, since
  \(\Im\cos t=\sin a\sinh H>0\).
  On the real outgoing cut use its horizontal descent instead.
* The left-side height profile increases strictly from zero.
  The unchanged formula is
  \[
   \partial_v\mathfrak b(iv,\theta-iA_0)
    =\pi-\vartheta_r(s+v)-\vartheta_r(s-v)>0,\quad
   \vartheta_r(w)=\arctan(\tan(\pi r)\tanh(\pi w)),
   \quad r=\theta/(2\pi),\ s=A_0/(2\pi).
   \tag{28}
  \]
* The right-side profile decreases to height \(K/(2\pi)\)
  and then increases strictly. The exact one-leg formulas
  (13)--(14) of that theorem only require
  \(0\le\theta\le\pi/2\) and the ordering \(H>K\).
  Its value at height zero is \((H+K)/2<m\).
* At a uniformly large finite height,
  \[
   \mathcal V(x+iv)=
       2\pi v-\frac{aH+bK}{2\pi}
                  +O(e^{1-2\pi v})>m+1 .
   \tag{29}
  \]
  This is the same original \(J\)-series expansion, uniform
  also at the two vertical sides.

Finally (23)--(24) provide the nondegenerate regular saddle
at level \(m\). The rectangle lemma gives exactly two strict
sublevel components. Each meets one vertical side, and the
two local descending sectors of this saddle lie in different
components. The lemma's Jordan argument needs only local
harmonic Morse coordinates; it does not require horizontal
descent or \(\Re F_{yy}<0\).

Choose small fixed endpoint cuts \(\alpha>0\),
\(1/3<\gamma<1/2\), inside the paid physical endpoint
intervals, and a small fixed cap height \(h_c>0\). By
continuity these intervals have paid upper collars through
height \(h_c\). Their points \(\alpha+ih_c\) and
\(\gamma+ih_c\) belong to the left and right sublevel
components, respectively. Each can therefore be joined to
its corresponding descending saddle germ by a compact
piecewise smooth strict-sublevel path in the open upper
half-strip.

Use a local holomorphic Morse coordinate at the saddle for
the intervening short segment. Orient the whole contour
from the left endpoint to the right endpoint. On the
adopted actual graph this is precisely the original
Gaussian orientation. The endpoint-component assignment is
locally constant in parameters: a compact strict-sublevel
connector persists under a small parameter change, and the
two sectors cannot enter the same component. Continuation
along each connected \(a\)-segment therefore retains the
original intersection sign \(+1\).

For each base parameter choose one such pair of paths and
a small saddle chart. Their remote compact pieces have
strict gaps, positive heights, and positive distances from
the vertical boundaries. These controls persist on a
parameter neighborhood by continuity. A finite cover of
(10) gives uniform path lengths, bounded heights and a
common positive remote gap. Short connectors accommodate
the moving saddle chart and the \(O(N^{-1})\) endpoint
roundings. No globally continuous choice of the remote
paths is required.

## 4. A complete lower rectangle without the first quarter

Put \(y=x-iv\), \(v\ge0\), and keep the original lower phase
\(F_-\). Its two shifted arguments have the same original
sidewise branches as in
[the complete lower-continuation proof, Section 2](research_mixed_next_shortened_edge_lower_continuation.md).
The Fourier-penalized lower rate is
\[
                    G_x(v)=\Re F_-(x-iv;t,u)-2\pi v .
 \tag{30}
\]
It extends continuously to \(x=0\) and \(v=0\).

We first pay the whole left vertical boundary. For one angle
\(z=\theta-iA_0\), use \(r,s,\vartheta_r\) from (28).
The exact shifted sine arguments at \(y=-iv\) give
\[
 \frac{d}{dv}\{\Re b(-iv,z)-\pi v\}
              =\vartheta_r(s+v)+\vartheta_r(s-v)\ge0 .
 \tag{31}
\]
The sign follows from oddness and monotonicity of
\(\vartheta_r\); it is strict if \(r,s>0\).
The original own logarithm has argument \(-\pi/2\),
which supplies the subtracted \(\pi v\).
The value at \(v=0\) is zero. The original lower \(J\)-series
in that same source gives the limit
\[
 \lim_{v\to\infty}\{\Re b(-iv,z)-\pi v\}
                      =\frac{\theta A_0}{2\pi}.
 \tag{32}
\]
Thus, including degenerate outgoing angles,
\[
 0\le G_0(v)\le\frac{aH+bK}{2\pi}
                    \le\frac{H+K}{4}<m-\frac1{25},
                  \qquad v\ge0 .
 \tag{33}
\]
Uniform continuity on \(0\le v\le1\), including the
integrated-logarithm endpoint, allows \(\alpha\) to be
chosen small enough that the entire column \(x=\alpha\)
has a fixed deficit in (30).

At the fixed deep height \(v=1\), the exact proof of
equations (15)--(22) of the cited lower theorem applies
unchanged on our larger angle family:
\[
 G_x(1)=\frac{aH+bK}{2\pi}+\Re\mathcal E(x),\quad
 |\mathcal E(x)|<\frac1{50},\qquad
                  G_x(1)<m-\frac1{50}.
 \tag{34}
\]
It uses only the independent bounds \(a,b\le\pi/2\),
\(H\le1\), \(K\le1/2\), with all primitive constants retained.

For every \(x\ge1/4\), the original lower derivative still
satisfies
\[
                           G_x'(v)<0\quad(v>0).
 \tag{35}
\]
Indeed, writing
\(\zeta=\cos(2\pi(x-iv))=p+iq\) and
\(\cos z=A_0+iB_0\), the imaginary numerator of
\((\zeta+\cos z)/(1-\zeta)\) is
\(q(1+A_0)+B_0(1-p)>0\).
Here \(p\le0,\ q>0,\ A_0,B_0\ge0\), including \(a=\pi/2\).
The original logarithmic lift is in \((0,\pi)\), fixed by
its limit \(i\pi\) at infinite lower depth. Summing two
legs and subtracting \(2\pi\) proves (35).
The column \(x=\gamma>1/3\) is consequently paid by its
real endpoint value.

The complete lower path can therefore be chosen as
\[
 \alpha-ih_c\ \longrightarrow\ \alpha-i\
 \longrightarrow\ \gamma-i\
 \longrightarrow\ \gamma-ih_c .
 \tag{36}
\]
All of it has a fixed strict deficit in the penalized
rate (30). The original half-grid roundings preserve these
gaps by uniform continuity. This argument uses neither a
reflected saddle ray nor a first-quarter real cut.

## 5. Literal finite contours and the saddle symbol

Use the exact canonical interpolation
\[
 \begin{split}
 B_N(y,z)&=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\\
 T_N(y;t,u)&=B_N(y,t)B_N(y,u).
 \end{split}
 \tag{37}
\]
It is holomorphic throughout \(0<\Re y<1/2\) at all
finite wire heights. On the lattice it equals the exact
product in (4). Keep the original half-grid rules
\[
 \alpha_N=(\lfloor N\alpha\rfloor+1/2)/N,\qquad
 \gamma_N=(\lceil N\gamma\rceil-1/2)/N .
 \tag{38}
\]
The original finite cotangent decomposition of
[the joined-contour theorem](research_mixed_next_shortened_edge_joined_contour.md)
then has the form
\[
 \begin{split}
 K_N^{<}(t,u)
  ={}&N\int_{\Gamma_+}
       \frac{T_N(y;t,u)}{1-e^{2\pi iNy}}\,dy
    +N\int_{\Gamma_-}
       \frac{T_N(y;t,u)}{e^{2\pi iNy}-1}\,dy\\
   &+\text{the two complete external caps}
      +\text{the two physical endpoint groups}.
 \end{split}
 \tag{39}
\]
Both paths are oriented left to right, with endpoints
\(\alpha_N\pm ih_c,\gamma_N\pm ih_c\).
Take \(\Gamma_+\) from Section 3 and \(\Gamma_-\) from
(36), with their small endpoint adjustments.
No internal real cut or unlisted residue is introduced.

On every fixed remote path the uniform zero-safe factorial
bound gives \( |T_N|\le C N^{-2}e^{N\mathfrak F}\).
At fixed positive upper height the first denominator is
bounded by two. At lower depth \(v\ge h_c\) the second is
bounded by \(2e^{-2\pi Nv}\). These are the full exact
denominators, not estimates for only their first Fourier
term. On either external half-grid cap the corresponding
denominator has modulus at least one. The endpoint collars
and Section 4 pay the caps. The original zero-safe finite
product bounds pay the entire omitted real endpoint sums,
including \(j=0\), all numerator zeros, the final shortened
row, and both parities.

The local saddle symbol requires a further check when a
shifted factorial argument leaves the positive-real strip.
All four shifted arguments at \(y_*\) avoid the negative
real axis and zero by (18)--(23); the own argument avoids
zero and one by (16). They range over fixed compact sets
with these exclusions. Midpoint Stirling in the defining
Gamma product gives
\[
 G_N(Nw-1/2)=\sqrt N\,e^{NJ(w)}(1+O(N^{-1}))
 \tag{40}
\]
uniformly on the positive-real side away from zero, also
through its imaginary boundary away from zero. On a
negative-real side with \(|\Im w|\) bounded below, use the
original exact reflection
\[
 \frac1{G_N(Nw-1/2)}
       =\frac{2\cos(\pi Nw)}{N}G_N(-Nw-1/2).
 \tag{41}
\]
One of its two exponentials dominates and the other is
exponentially small. With the corresponding original
\(J_{\rm side}(w)=-J(-w)\pm i\pi w\), (41) gives
the reciprocal of (40) with the same leading coefficient.
Compact overlapping charts cover transitions through
\(\Re w=0\). There is no relative expansion through a
factorial zero.

Applying this to (37), and the original own half-step
shift, yields near the saddle
\[
 T_N(y;t,u)=
   \frac{e^{NF(y;t,u)}}{4N^2\sin^2(\pi y)}
                            (1+O(N^{-1})).
 \tag{42}
\]
All errors are holomorphic and uniform on the fixed local
charts. The full upper denominator is \(1+O(e^{-cN})\)
there because the saddle height has a positive uniform
lower bound. The oriented local Morse integral thus gives
\[
 N\cdot N^{-2}\cdot N^{-1/2}
 \frac{\sqrt{2\pi}}{4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*)}}
 e^{N\psi}(1+O(N^{-1})),
 \tag{43}
\]
with the sign calibrated in Section 3.
Every other term of (39) is exponentially smaller.
This proves (5)--(8), retaining the algebraic Gaussian
error as such.

## 6. Independent neighborhoods and scope

All saddle and cut separations above are strict on a compact
parameter family. The explicit \(W,D_0\), the original phase,
and the coefficient (7) consequently extend holomorphically
to a fixed independent neighborhood. For each base pair
retain its chosen finite remote paths and local saddle
chart. The original sidewise upper rates are jointly
continuous, including their moving zeros and cuts, so the
strict remote gaps persist on a small independent parameter
neighborhood. A finite cover makes the bounds uniform.

The physical endpoint estimates also persist on these
neighborhoods. The original uniform reciprocal-factorial
bound applies to all shifted arguments in a fixed compact
subset of \((-1,1)+i\mathbb R\), including their cuts.
For the own factorial, uniformly for \(0\le x\le1/2\),
\[
       N|J(x+1/(2N))-J(x)|=O(1+\log N).
 \tag{44}
\]
The zero row is exactly one. Thus every original physical
endpoint row has at most polynomial cost beyond its
continuous upper rate, at both parities. These estimates
do not rely on persisting real quadrant signs outside the
base family.

The normalized error in (9) is holomorphic on the larger
neighborhood and uniformly \(O(N^{-1})\) there. Cauchy's
estimate on a smaller fixed neighborhood proves (9).

The first complete edge has a separate existing source bound:
[the complete-edge gap, Theorem 2 and Corollary 3](research_internal_pair_complete_edge_gap.md)
gives
\[
 K_N(t,0)=\exp\{N\psi(t,0)+O(\log N)\}
\]
on a fixed complex neighborhood of
\(0\le\Re t\le\pi/2,\ -107/100\le\Im t\le0\).
That theorem includes the full radical and requires no
\(|A|<1\) restriction. Combining its polynomial upper bound
with (5) gives, on a smaller independent neighborhood of (3),
\[
 |K_N(t,0)K_N^{<}(t,u)|
       \le C N^A
         \exp\{N\Re(\psi(t,0)+\psi(t,u))\}.
 \tag{45}
\]
This is a bound for the complete two-factor source on the
positive horizontal family. The full inner trace and the
remaining outer observation retain their contour obligations.
