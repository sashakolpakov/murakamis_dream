# The shortened edge at mixed angular heights

Private finite-source proof, 8 November 2026. The shortened second
edge has its original Gaussian packet on the actual mixed-height
family needed by the middle negative inner horizontal. The main
wire contour follows the half-plane of its saddle. Both Fourier
corrections are estimated separately, so the proof also covers a
saddle on the real sampling line.

All reflection terms, physical endpoint groups, exact cutoffs and
both parities are retained. No mathematical numerical evaluation or
frozen-source edit is used.

## 1. Actual family and statement

Keep
\[
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},
 \quad t_*(u)=a_*(u)-iH(u),\quad 1/2<H(u)<1 .
 \tag{1}
\]
These are the original cubic family and heights. Fix any
\(0<a_L<a_R\le\pi/2\). For the proof use the compact signed
height family
\[
 \mathcal M=\{(t,u):u\in\mathcal U_+,\quad
         t=a+iS,\quad a_L\le a\le a_R,\quad -H(u)\le S\le H(u)\}.
 \tag{2}
\]
The mixed-height target is its face \(S=H(u)\). The face
\(S=-H(u)\) has the adopted
[positive-horizontal packet](research_mixed_next_shortened_edge_positive_horizontal_packet.md).

Keep the unchanged finite source
\[
 \begin{gathered}
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^{<}(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u),\\
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D_0=A+B-AB,\quad W=AB/D_0,\quad
 y_*=\pi^{-1}\arctan\sqrt W .
 \end{gathered}
 \tag{3}
\]
The Newton normalization and literal odd middle-row deletion are
those of [the exact low-edge theorem](research_mixed_next_outer_exact_low_edge_reduction.md).

**Theorem 1.** On a fixed independent complex neighborhood of
\(\mathcal M\), uniformly at both parities,
\[
 K_N^{<}(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                                      (1+O(N^{-1})),
 \qquad
 a_e(t,u)=\frac{1}{4\sqrt{D_0}\,W^{1/4}}\ne0 .
 \tag{4}
\]
The phase, charge and principal powers are the original ones.
The normalized error is holomorphic and is \(O(N^{-1})\),
with all fixed parameter derivatives on a smaller neighborhood.
Only the shortened edge is estimated by this theorem.

## 2. Original action and cuts throughout the height interpolation

The signed-box phase from
[negative-horizontal phase, Section 1](research_mixed_next_inner_three_negative_horizontal_phase.md)
supplies the original holomorphic primitive on (2):
\[
 d\psi=-\pi^{-1}\{\operatorname{arsinh}(\tan(t/2)\cos(u/2))\,dt
             +\operatorname{arsinh}(\tan(u/2)\cos(t/2))\,du\}.
 \tag{5}
\]
Both returns are principal and cut-safe. Its complete constant is
unchanged. The same elementary guards give
\[
 |1-A|<4/5,\quad |1-B|<4/7,\quad \Re D_0>19/35 .
 \tag{6}
\]
The factorization (12) in the positive-horizontal packet depends
only on \(|S|\), not on its sign. It therefore proves
\[
 \Re(1/A)>10/13,\qquad \Re(1/B)>14/15,\qquad
                         \Re(1/W)>137/195.
 \tag{7}
\]
Thus \(W,D_0\) stay in compact subsets of the right half-plane.
The saddle in (3) lies in \(0<\Re y_*<1/2\); its imaginary
part may be positive, negative, or zero.

The original one-leg phase and real upper envelope are
\[
 \begin{split}
 b(y,z)&=-J(1/2-y+z/(2\pi))
         -J(1/2-y-z/(2\pi))-2J(y),\\
 F(y;t,u)&=b(y,t)+b(y,u),\qquad
 \mathcal V(y)=\mathfrak b(y,t)+\mathfrak b(y,u).
 \end{split}
 \tag{8}
\]
Use exactly the sidewise reciprocal-factorial branches of
[the uniform factorial theorem](research_uniform_factorial_and_boundary_decay.md).
For \(z=\theta+iA_0\), its interior zero cut starts at
\[
       y=\frac12-\frac{\theta}{2\pi}-\frac{iA_0}{2\pi}
 \tag{9}
\]
and runs horizontally to the right boundary. In particular
the \(t\) cut is lower when \(S>0\), while the \(u\) cut is
upper. The other shifted zero is outside the open half-strip.

Here is a cut-force bound requiring no common sign of the
angular heights. Put \(C=\cosh|A_0|\), and
\(q_0=\cos\phi\in[0,1]\) on the cut, where
\(\phi=\pi-2\pi\Re y\). The exact own-leg calculation of
[upper terminal regions, equations (12)--(15)](research_mixed_next_shortened_edge_upper_terminal_regions.md)
and its conjugate give
\[
 |\cos(2\pi y)+\cos z|\le q_0\sqrt{2C^2-1},
 \qquad |1-\cos(2\pi y)|=C+q_0 .
 \tag{10}
\]
Also \(|\cos(2\pi y)|\le C\). If
\(|\cos z'|\le M\) for the other angle, the full force is at most
\[
 \frac{q_0\sqrt{2C^2-1}(C+M)}{(C+q_0)^2}
 \le\frac{\sqrt{2C^2-1}}{C+1}\frac{C+M}{C+1}.
 \tag{11}
\]
The inequality uses the increase of \(q_0/(C+q_0)^2\) on
\([0,1]\), since \(C\ge1\). The first factor on the right increases
with \(C\); for \(M\ge1\), the second is at most \((1+M)/2\).
Consequently the full force on the \(u\) cut is at most
\[
        \frac{13\sqrt{79}}{150}<1,
              \qquad 13351<22500,
 \tag{12}
\]
and on the \(t\) cut it is at most
\[
        \frac{15\sqrt{103}}{182}<1,
              \qquad 23175<33124.
 \tag{13}
\]
We used only \(\cosh(1/2)<8/7\) and \(\cosh1<8/5\).
The estimates include a starting zero by continuity.

The exact critical identity is
\[
 e^{F_y}-1=
 -\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},
                      \qquad z_y=\tan(\pi y).
 \tag{14}
\]
The full open strip \(0<\Re y<1/2\) maps to \(\Re z_y>0\).
Its unique finite algebraic root is \(z_y=\sqrt W\).
The force is one there, so (12)--(13) prevent it from crossing
any original cut or zero, including a real cut when an angular
height is zero. Continue \(S\) from \(-H(u)\) to its desired
value. The original logarithmic \(F_y(y_*)\) is continuous,
belongs to \(2\pi i\mathbb Z\), and starts at zero. Hence
\[
 F_y(y_*;t,u)=0,\quad F(y_*;t,u)=\psi(t,u),\quad
 -F_{yy}(y_*)=\frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0 .
 \tag{15}
\]
The critical-value equality follows by continuation of the
original closed primitive (5), not by assigning a new constant.
The coefficient in (4) is the same principal-root expression
already calibrated on the initial face of (2).

Write \(m=\Re\psi(t,u)\). A uniform endpoint gap holds on all
of (2):
\[
                         m>\frac{|S|+K}{2}+\frac1{25}.
 \tag{16}
\]
For \(S\le0\) this is the adopted independent-box endpoint
theorem. For \(S\ge0\), the product
\(\tan(t/2)\cos(u/2)\) has nonnegative imaginary part, while
\(\tan(u/2)\cos(t/2)\) has nonpositive imaginary part.
The imaginary part of a principal return has the same sign as
its argument: if the return is \(\xi+i\nu\), then
\(\Im\sinh(\xi+i\nu)=\cosh\xi\sin\nu\), with
\(|\nu|<\pi/2\). Thus increasing either mixed depth increases
\(\Re\psi\). Real-angle monotonicity gives
\[
 \Re\psi(a+iS,b-iK)\ge\psi(a,b)\ge\psi(\pi/2,\pi/2)
          >50/63 .
 \tag{17}
\]
Since \(S+K\le3/2\), the excess over the half-endpoint rate
is greater than \(50/63-3/4=11/252>1/25\). All returns in
this argument are precisely those licensed by (5).

## 3. The real row profile has no local minimum

This verifies the bottom-boundary hypothesis needed in either
wire half-plane. Put \(v=\sin^2(\pi x)\), \(0<x<1/2\), and
\[
       q_A(v)=\frac{|A-v|}{v},\qquad
       q_B(v)=\frac{|B-v|}{v}.
 \tag{18}
\]
The real derivative of the original row profile is
\(\partial_x\mathcal V(x)=\log(q_Aq_B)\).
Away from a numerator zero,
\[
 \frac{d}{dv}\log q_A(v)
       =\frac{\Re A\,v-|A|^2}{v|A-v|^2},
 \tag{19}
\]
and similarly for \(B\).
Both real parts are at least \(1/2\), so both derivatives
are negative for \(v<1/2\).

We claim that whenever \(q_Aq_B\ge1\), both derivatives
in (19) are strictly negative. Suppose first that the
\(A\)-derivative is nonnegative. Then \(v\ge1/2\) and
\[
                  q_A(v)^2\le1-\frac1{2v}\le\frac12.
 \tag{20}
\]
For \(v\in[1/2,1]\), \(q_B(v)^2\le64/49\). To check
this last bound explicitly, put \(w=1/v\in[1,2]\),
\(C=\cosh K\le8/7\), and \(c=\cos b\in[0,1]\). The
expression
\[
 q_B^2=1-(1+C c)w+\frac{(C+c)^2w^2}{4}
 \tag{21}
\]
is convex separately in \(w\) and \(c\). Its four endpoint
values are bounded by \(64/49\). Their maxima over
\(1\le C\le8/7\) have the same bound. Hence
\((q_Aq_B)^2\le32/49<1\), a contradiction.

If instead the \(B\)-derivative is nonnegative, then
\[
                    q_B^2\le1-w/2,\qquad 1\le w\le2 .
 \tag{22}
\]
The analogue of (21), with \(\cosh|S|\le8/5\), and
convexity in \(\cos a\), gives
\[
 q_A^2\le
 \max\left\{1-w+\frac{16w^2}{25},
                         (1-13w/10)^2\right\}.
 \tag{23}
\]
The first expression is at most \(39/25\), by convexity
on \([1,2]\), so its product with (22) is at most
\(39/50<1\). For the second, on \(1\le w\le3/2\) it is
at most \(361/400<1\), while (22) is at most \(1/2\).
On \(3/2\le w\le2\), it is at most \(64/25\), while
(22) is at most \(1/4\). Again the product is strictly
less than one. This proves the claim.

The continuous force modulus \(q_Aq_B\) starts at infinity
as \(v\downarrow0\), and ends below one, since
\[
              q_A(1)q_B(1)=|1-A||1-B|<16/35 .
 \tag{24}
\]
At any point where it is one, the preceding claim gives a
strictly negative derivative. There is therefore exactly
one such crossing, from above to below. Numerator zeros
have modulus zero and cannot be additional crossings.
The real row profile consequently increases to one strict
maximum and then decreases; it has no interior local
minimum. Its logarithmic derivatives at a zero are used
only through their integrable one-sided limits.

If \(\Im W=0\), the original saddle \(y_*\) is real.
Equations (14)--(15) identify it with this unique maximum,
whose value is \(m\), and (19) gives
\(\Re F_{yy}(y_*)<0\). The real main interval itself then
supplies the local Gaussian and strict remote gaps.

## 4. The main contour in the saddle's half-plane

The sidewise envelope \(\mathcal V\) is continuous and
subharmonic in either open half-strip. At each original
cut its normal derivative jumps upward by \(2\pi\).
The starting-zero flux is \(O(\epsilon|\log\epsilon|)\).
These are exactly the original reciprocal-reflection
identities used in
[upper continuation, Section 2](research_mixed_next_shortened_edge_upper_continuation.md),
with conjugation for a lower cut. On each cut (12)--(13)
give a strict horizontal descent direction, so no cut
point or starting zero is a local minimum.

The unweighted left-side rate increases strictly with the
distance from the real axis, for either sign of either
angular height. Indeed the one-leg outward derivative is
\[
 \pi\ \pm\
 \{\vartheta_r(s+v)+\vartheta_r(s-v)\},\qquad
 \vartheta_r(w)=\arctan(\tan(\pi r)\tanh(\pi w)),
 \tag{25}
\]
where \(r=\theta/(2\pi)\in[0,1/4]\) and
\(s=|\Im z|/(2\pi)\). The sum has absolute value at most
\(2\pi r\le\pi/2\). The rate starts at zero. Thus its
strict sublevel below \(m>0\) is nonempty and connected.
At large upper or lower height the full unweighted rate
is \(2\pi v+O(1)\), uniformly on the family, so a fixed
finite outer horizontal lies above \(m+1\).

We next prove connectedness of the right-side sublevel in
the half-plane containing the saddle. If \(S\le0\), both
angular heights are lower: the right-side rate decreases
to the smaller of the two cut heights, then increases.
The proof in the original upper-continuation theorem
applies with the labels exchanged if necessary. The
saddle is upper, unless it is real.

Now suppose \(S>0\). Write
\[
 \cos(a-iS)=P_t+iQ_t,\qquad
 \cos(b-iK)=P_u+iQ_u,\qquad Q_t>0,\quad Q_u\ge0 .
 \tag{26}
\]
The actual first cosine is \(P_t-iQ_t\). On the central
right-side height interval
\(-S/(2\pi)<v<K/(2\pi)\), the original derivative is
\[
 g(C_v)=\Arg(P_t-C_v+iQ_t)-\Arg(P_u-C_v+iQ_u),
                     \qquad C_v=\cosh(2\pi v).
 \tag{27}
\]
For \(Q_u>0\) both arguments belong to \((0,\pi)\), so
the sign of \(g\) is the sign of
\[
              Q_tP_u-Q_uP_t+C_v(Q_u-Q_t).
 \tag{28}
\]
Outside the displayed central height interval the derivative
has the fixed outward sign: it is positive above the
outgoing cut and negative below the incoming cut. At a cut
its jump is positive, so that point cannot be a local maximum.

An upper-side local maximum at \(v>0\) would require a
downward crossing in (28), hence \(Q_t>Q_u\). At its
stationary value \(C=C_v\), write the aligned vectors as
\[
 P_t-C+iQ_t=\lambda e^{i\theta},\qquad
 P_u-C+iQ_u=\mu e^{i\theta},\qquad
                  \lambda>\mu>0,\quad0<\theta<\pi .
 \tag{29}
\]
Each individual right-boundary force is strictly less than one:
\[
       |\cos z-C|<C+1\qquad(C\ge1).
 \tag{30}
\]
For example,
\[
 |\cos z|^2-1\le\sinh^2|\Im z|<39/25<2
                       \le2C(1+\Re\cos z).
 \tag{31}
\]
The outgoing bound is stronger, and \(\Re\cos z\ge0\)
on our angle box. Thus \(\lambda\mu<(C+1)^2\).
Using \(1/W=1/A+1/B-1\), direct subtraction now gives
\[
 \Im(1/W)=
 \frac{2\sin\theta(\lambda-\mu)
                  ((1+C)^2-\lambda\mu)}
 {|1+P_t+iQ_t|^2\,|1+P_u+iQ_u|^2}>0 .
 \tag{32}
\]
Such an upper-side maximum therefore forces \(\Im W<0\).
It is impossible when the saddle lies in the upper half-plane.
Similarly, a lower-side local maximum requires \(Q_t<Q_u\),
because \(C_v\) decreases as negative \(v\) increases.
The reversed inequality in (32) then forces \(\Im W>0\).
It is impossible when the saddle lies in the lower half-plane.

There are no unlisted flat maxima. Unless both cosine vectors
coincide, (28) is a nonzero affine function of \(C_v\).
A zero at \(v=0\) is not an extremum: the derivative in
(27) has the same sign on both sufficiently small sides.
Coincident vectors make \(W\) real, which is already
handled by the real main profile. If \(Q_u=0\), the same
conclusion follows directly: for \(K=0\) the right-side
minimum is at zero; for \(b=0,K>0\), the only sign change
on the negative side is a minimum, at
\(-\min(S,K)/(2\pi)\). The upper side increases.
These are also the original one-leg formulas with their
zero-angle limits; no argument is assigned at a zero.

The right-side rate starts at \((|S|+K)/2<m\) and tends
to infinity outward. In the half-plane of a nonreal saddle
it has no local maximum, so its strict sublevel below \(m\)
is connected. Section 3 excludes real-boundary minima,
and regular interior points are harmonic. Equations
(12)--(15) exclude other cut minima and give the unique
nondegenerate interior saddle.

Apply the adopted rectangle/component lemma in that
half-strip (reflecting the wire coordinate for a lower
saddle). Its two descending sectors reach the two different
side components. Since the real physical endpoints have
the strict gap (16), small endpoint collars connect those
side components to fixed real cuts \(\alpha,\gamma\),
where \(0<\alpha<\gamma<1/2\). We obtain a main contour
from \(\alpha\) to \(\gamma\), through the saddle, with
strict gaps off a small local Morse segment.
The cuts may be chosen outside the compact range of
\(\Re y_*\), while remaining in the paid endpoint intervals.

At \(\Im W=0\) use the real main contour from Section 3.
Its strict remote gaps and nondegenerate local Gaussian
persist on an independent neighborhood, with a small local
deformation through the continued saddle. Thus no shrinking
wire-height denominator is needed near this transition.
For nonreal saddles use the compact strict-sublevel paths
just constructed. A finite cover gives uniform path lengths,
bounded heights, and fixed remote gaps throughout (2).
The left-to-right Morse orientation continues from the
original positive face and across the real-saddle charts;
the intersection coefficient remains \(+1\).

## 5. Both complete Fourier corrections are paid

We give fixed upper and lower alias paths, independent of
the sign or size of the saddle height. Their rate is
\(\mathcal V(x\pm iv)-2\pi v\).

First, on the left boundary the same shifted-logarithm
calculation as (25) shows that each one-leg penalized rate
starts at zero and varies monotonically toward a limit of
magnitude \(\theta|\Im z|/(2\pi)\). Therefore
\[
 \mathcal V(\pm iv)-2\pi v
       \le\frac{a|S|+bK}{2\pi}
       \le\frac{|S|+K}{4}<m-\frac1{25}.
 \tag{33}
\]
Both signs are included.

For a precise right-boundary estimate, write
\[
 r=\theta/(2\pi),\quad
 L(r,s)=\Re J(r+is),\quad
 L(r,-s)=L(r,s),\quad
 \partial_s L(r,s)=-\omega_r(s),
 \quad
 \omega_r(s)=\arctan(\cot(\pi r)\tanh(\pi s)).
 \tag{34}
\]
Use the limiting formulas if \(r=0\).
For \(z=\theta+i2\pi s\), original reciprocal reflection gives
\[
 \mathfrak b(1/2+iv,z)
       =-L(r,s-v)+L(r,s+v)+\pi|s+v|.
 \tag{35}
\]
If \(s\ge0\), the \(L\)-difference is nonpositive, so
subtracting \(\pi v\) gives a bound \(\pi s\).
If \(s=-k<0\), the difference is at most
\(\pi\min(v,k)\), since \(|\partial_sL|\le\pi/2\).
Separating \(v\le k\) and \(v\ge k\) again gives the
bound \(\pi k\). Conjugation supplies the other wire sign.
Consequently
\[
 \mathcal V(1/2\pm iv)-2\pi v
                      \le\frac{|S|+K}{2}<m-\frac1{25}.
 \tag{36}
\]
These estimates retain all cuts and their zero-angle limits.

At the fixed depths \(v=1\), the original \(J_+\) and \(J_-\)
series in
[lower continuation, equations (15)--(22)](research_mixed_next_shortened_edge_lower_continuation.md)
apply to both signs of the angular heights. The polynomial
part of the penalized two-leg rate has absolute value at
most \((a|S|+bK)/(2\pi)\); its remainder has modulus less
than \(1/50\). Hence
\[
                 \mathcal V(x\pm i)-2\pi
                              <m-\frac1{50}.
 \tag{37}
\]
Uniform continuity on \(0\le v\le1\) moves (33),(36)
to fixed interior columns \(x=\alpha\) and \(x=\gamma\).
Choose these inside the uniform paid physical endpoint
intervals, and choose a small fixed \(h_c>0\) with paid
unweighted endpoint collars. Both complete alias paths
can be taken as
\[
 \alpha\pm ih_c\longrightarrow\alpha\pm i
       \longrightarrow\gamma\pm i
       \longrightarrow\gamma\pm ih_c .
 \tag{38}
\]
Their gaps are uniform on (2), including real saddles.

## 6. Exact main-charge separation and finite normalization

Keep the original canonical interpolation
\[
 B_N(y,z)=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\quad
 T_N(y;t,u)=B_N(y,t)B_N(y,u).
 \tag{39}
\]
It is holomorphic on \(0<\Re y<1/2\) at every finite
height. Put
\[
 \alpha_N=(\lfloor N\alpha\rfloor+1/2)/N,\qquad
 \gamma_N=(\lceil N\gamma\rceil-1/2)/N,\qquad
                              \zeta=e^{2\pi iNy}.
 \tag{40}
\]
The exact joined representation is the upper integral
\(N\int T_N/(1-\zeta)\), the lower integral
\(N\int T_N/(\zeta-1)\), the original two external caps,
and the original two physical endpoint sums.
Split
\[
                       \frac1{1-\zeta}
                            =1+\frac{\zeta}{1-\zeta}.
 \tag{41}
\]
Move only the unweighted entire integral to the main contour
of Section 4, whose endpoints are now \(\alpha_N,\gamma_N\).
The exact added endpoint terms are
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy
       +N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy .
 \tag{42}
\]
They follow by Cauchy's theorem and retain their displayed
orientations. They join the original external caps; all are
paid by the unweighted endpoint collars. No real residue
is crossed by either Fourier correction.

Thus the exact remaining currents are an unweighted main
integral and the two complete aliases
\[
 N\int_{\Gamma_+}T_N\,\frac{\zeta}{1-\zeta}\,dy,\qquad
 N\int_{\Gamma_-}T_N\,\frac1{\zeta-1}\,dy .
 \tag{43}
\]
Use the rounded paths (38). At depths \(v\ge h_c\), their
respective multipliers are bounded by \(2e^{-2\pi Nv}\).
Together with the original zero-safe factorial bounds and
(33)--(38), this pays both whole denominators with a fixed
exponential gap. The external half-grid denominators have
modulus at least one. The entire omitted physical endpoint
groups retain their uniform finite \(O(\log N)\) factorial
cost, including \(j=0\), every numerator zero, the terminal
shortened row, and both parity conventions.

Near the selected saddle all shifted factorial arguments
avoid their original cuts and zeros by (12)--(15).
The sectorial midpoint expansion and, where necessary,
the exact two-term reciprocal reflection give the original
local symbol
\[
 T_N(y;t,u)=
 \frac{e^{NF(y;t,u)}}{4N^2\sin^2(\pi y)}
                                     (1+O(N^{-1})).
 \tag{44}
\]
This is the same off-cut continuation proved explicitly in
the positive-horizontal packet; no relative symbol is
asserted at a zero. The selected main contour and (15)
give its original Gaussian coefficient
\[
 N\cdot N^{-2}\cdot N^{-1/2}
 \frac{\sqrt{2\pi}}
     {4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*)}}
                =N^{-3/2}a_e(t,u).
 \tag{45}
\]
The principal expression in (4) has the calibrated sign.
Every other term is exponentially smaller. Finite-cover
continuity of the remote source bounds, the physical-row
estimates and the local symbol gives a fixed independent
complex neighborhood, including the real-saddle transition.
Cauchy's estimate after exponential normalization proves
the derivative assertion. This establishes Theorem 1.

## 7. The actual middle negative angular interval

Take \(a_L=\eta\), where \(\eta>0\) is the adopted center cut,
and \(a_R=5\pi/12\). At the actual negative inner point
\(t=-a-iH(u)\), evenness gives
\[
                    K_N^{<}(t,u)=K_N^{<}(a+iH(u),u).
 \tag{46}
\]
The original signed primitive likewise gives
\(\psi(-a-iH,u)=\psi(a+iH,u)\).
The full first edge has its separate complete-edge
polynomial bound, using evenness and conjugation:
\[
 |K_N(-a-iH,0)|
        \le C N^B e^{N\Re\psi(-a-iH,0)} .
 \tag{47}
\]
Combining (4), (46)--(47), the bounded sine, and the exact
double-pole multiplier
\[
 |W_N(-a-iH)|\le C e^{-NH},
 \tag{48}
\]
therefore bounds the original full angular integrand by a
polynomial times \(e^{N\Re\Phi(-a-iH,u)}\), with the
unchanged crossing and charge.

The adopted
[negative-horizontal phase theorem, equations (19)--(21)](research_mixed_next_inner_three_negative_horizontal_phase.md)
has a fixed \(\epsilon_->0\) such that
\[
            \Re\Phi(-a-iH(u),u)\le\Re S(u)-\epsilon_-
                       \qquad(0\le a\le\pi/2).
 \tag{49}
\]
After polynomial absorption, both the pointwise complete
integrand on \(\eta\le a\le5\pi/12\) and its absolute
integral, including the original \(N^2/\pi\), are
\[
                         O(e^{N(\Re S(u)-\epsilon_-/2)}).
 \tag{50}
\]
All angular Fourier charges are included by (48).

Together with the adopted center and far-negative bounds,
(50) pays the entire remaining negative part of the
critical-height horizontal. Consequently the
[partial-horizontal packet](research_mixed_next_inner_three_partial_horizontal_packet.md)
extends to the oriented segment
\([-\pi/2-iH(u),\,\pi/2-iH(u)]\), with exactly its same
nonzero coefficient and \(C_{N,3}N^{-3/2}\) normalization.
No moving-endpoint parameter derivatives are inferred.
The connectors to the original far angular endpoints and
the remaining outer observation are still separate.
