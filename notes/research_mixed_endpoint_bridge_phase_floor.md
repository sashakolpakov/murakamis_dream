# The original endpoint phase on the lower bridge strip

Research deduction, 7 November 2026. The original endpoint critical
phase continues on the entire negative-height strip used by the
new real-row tail estimate. Its auxiliary critical point stays in
the original primitive chamber, even when its height is negative.
Lowering the private height strictly increases the real critical
action. A uniform action floor then pays every auxiliary row in
the upper half of the complete finite continuation.

The real-cut comparisons and retained contour currents remain
separate. This is not a complete endpoint-packet theorem on the
strip and does not enclose the actual continued cap path there.
No numerical evaluation or saved replay is used.

## 1. Original phase and branch

Use precisely
\[
 \begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\qquad p=e^{2\pi ie},\quad
                              \omega=e^{2\pi iu_c(e)},\\
 (p-5)\omega^2+2(p+1)\omega+(p-1)&=0 .
 \end{split}                                                    \tag{1}
\]
The branch is the original upper-half-plane endpoint root
and the original zero logarithmic lift, as in
[the complex-index endpoint theorem](research_complete_boundary_complex_index.md)
and [the half-face critical-point proof](research_mixed_half_face_cap_critical_point.md).
All primitive constants are unchanged.

Let
\[
 \mathcal E=
 \{e=E-i\eta:\ 6/25\le E\le49/100,\quad0\le\eta\le3/50\}.
                                                                  \tag{2}
\]
Then \(p\) is in the upper half-plane and
\[
             1\le |p|<3/2,\qquad \Re p<3/20.                 \tag{3}
\]
Indeed \(2\pi\eta\le3\pi/25<2/5<\log(3/2)\).
Also
\(\cos(2\pi E)\le\sin(\pi/50)<1/10\), and
\(\Re p=|p|\cos(2\pi E)\). These are elementary written
inequalities, not enclosures obtained by evaluating a root.

For upper-half-plane \(p\), the original endpoint quadratic
has exactly one upper-half-plane root. One can use the root
count in the half-face proof directly: a real root would
make
\[
                   p=\frac{5\omega^2-2\omega+1}{(\omega+1)^2}
                                                                  \tag{4}
\]
real, while \(\omega=-1\) is not a root. The leading
coefficient never vanishes in the upper half-plane, and
the discriminant \(16(2p-1)\) is nonzero. The known initial
root count therefore continues throughout that half-plane.
The selected root is simple and holomorphic. Choose
\(\Log\omega\) with argument in \((0,\pi)\).

## 2. No private-minus-auxiliary wall on the whole strip

**Lemma 1.** On (2), the original branch obeys
\[
                0<\Re u_c(e)<E<1/2,\qquad F_u(e,u_c(e))=0.
                                                                  \tag{5}
\]
It extends holomorphically, with these primitive arguments
regular, to a fixed neighborhood of the compact strip.

*Proof.* The upper root already gives \(0<\Re u_c<1/2\).
We exclude a positive real value of \(p/\omega\).
Suppose \(p=s\omega\), \(s>0\). Equation (1) becomes
\[
 f_s(\omega):=s\omega^3+(2s-5)\omega^2+(s+2)\omega-1=0.
                                                                  \tag{6}
\]
Its coefficients are real and \(\omega\) is nonreal.
The third root \(\alpha\) is therefore real, with
\[
              \alpha|\omega|^2=1/s,\qquad
                       \alpha=\frac{s}{|p|^2}\le s.           \tag{7}
\]
In particular \(\alpha>0\) and is the unique real root.
Since the leading coefficient is positive,
\(f_s(s)\ge0\). But
\[
 f_s(s)=s^4+2s^3-4s^2+2s-1
                    =(s-1)(s^3+3s^2-s+1).                  \tag{8}
\]
The cubic in the last factor is positive for every \(s>0\):
for \(s\le1\), group its last terms as \(1-s\);
for \(s\ge1\), group \(s^3-s\). Thus \(s\ge1\).

Vieta's second relation in (6) supplies, independently,
\[
 1+\frac2s=|\omega|^2+2\alpha\Re\omega
             =\frac{|p|^2}{s^2}+\frac{2\Re p}{|p|^2},
 \]
or
\[
              s^2\left(1-\frac{2\Re p}{|p|^2}\right)
                                      +2s=|p|^2.             \tag{9}
\]
By (3), the left side is at least
\((7/10)s^2+2s\ge27/10\), whereas the right side is
less than \(9/4\). This contradiction excludes the ray.

At \(\eta=0\), the original real-index branch satisfies
\(0<\Re u_c(E)<E\). Continue \(p\) radially along
\(E-i[0,\eta]\). Both \(p\) and \(\omega\) stay in the
upper half-plane; the ray just excluded prevents
\(\arg p-\arg\omega\) from vanishing. Hence the same
strict inequality holds along the entire segment.
All arguments \(u_c,1/2-u_c,e-u_c\) now have real parts
strictly between zero and \(1/2\).

The exponentiated endpoint equation is unchanged.
The original \(F_u\) is an integral multiple of \(2\pi i\)
and equals zero at the initial real parameter; the regular
continuation just proved preserves that value. This
proves (5), with the actual logarithmic lift. Simplicity,
compactness and the positive strip distances give the
claimed fixed neighborhood. \(\square\)

## 3. Height ordering and monotonicity of the actual action

**Lemma 2.** Throughout (2),
\[
                \Im u_c(e)>\Im e,\qquad
                \Im S'(e)>0,\qquad
                \Re S(E-i\eta)\ge\lambda(E),\quad
                       \lambda(E):=\Re S(E).                \tag{10}
\]
The last inequality is strict when \(\eta>0\).

*Proof.* Suppose \(\Im u_c\le\Im e\le0\). On the
primitive chamber in (5),
\[
 \Im F_u
 =2\Arg\sin\pi(1/2-u_c)-3\Arg\sin\pi u_c
                  +\Arg\sin\pi(e-u_c)+\pi E.                \tag{11}
\]
The first sine has nonnegative height, the second
nonpositive height, and the third nonnegative height.
For a sine with real part in \((0,1/2)\), its argument
has the sign of its height and modulus less than \(\pi/2\).
Every term before \(\pi E\) in (11) is consequently
nonnegative. Since \(E>0\), this contradicts \(F_u=0\).
The first assertion in (10) follows.

Critical stationarity gives the original envelope derivative
\[
                    S'(e)=-J'(e-u_c)+i\pi u_c .              \tag{12}
\]
Now \(e-u_c\) has negative height and real part in
\((0,1/2)\). Therefore
\[
       \Im S'(e)=-\Arg\sin\pi(e-u_c)+\pi\Re u_c>0.           \tag{13}
\]
Since \(\partial_\eta\Re S(E-i\eta)=\Im S'(E-i\eta)\),
integration on the full radial segment proves (10).
No sign of \(\Im u_c\) itself is asserted. \(\square\)

## 4. A quantitative floor with the original additive constant

The exact real-index curvature identity is
\[
 -\frac{\lambda''(E)}{\pi}
   =\cot\pi E+\frac{2}{\sin\pi E}
                        \Re\frac1{\sqrt{2-e^{-2\pi iE}}}.
                                                                  \tag{14}
\]
It is the original endpoint identity used, for example,
in Section 2 of
[the fixed-cut proof](research_mixed_next_half_face_fixed_cut_obstruction.md).
The square root has its original positive real part.
For \(6/25\le E\le49/100\),
\[
 \cot\pi E<9/8,\qquad \sin\pi E>2/3,\qquad
                  |\sqrt{2-e^{-2\pi iE}}|>7/5.               \tag{15}
\]
Indeed \(\pi E>3/4\), and
\(\tan(3/4)\ge57/64>8/9\), while the sine lower
polynomial at \(3/4\) exceeds \(2/3\).
Furthermore \(\cos2\pi E<1/10\), so
\[
 |2-e^{-2\pi iE}|^2=5-4\cos2\pi E>23/5>4.
 \]
Taking square roots twice and using \(\sqrt2>7/5\)
proves the last inequality in (15).
Equations (14)--(15) give the strict uniform bound
\[
              0<-\lambda''(E)
                 <\frac{183\pi}{56}<11.                    \tag{16}
\]

Use only the already printed scalar consequences of the
[original seam-source replay](../repro/results/research-mixed-cap-seam-source-bounds-replay.json),
whose SHA256 is
\[
 \texttt{8d907c890073955f7e1122abc78f1334ab00a885959d839316d3852e2a64f3f8}.
 \]
The complete outward displays are reproduced in Section 1 of
[the half-cap action upper theorem](research_mixed_half_face_cap_action_upper.md).
Their digits and printed error radii directly imply
\[
              \lambda(7/20)>108/125,\qquad
                        |\lambda'(7/20)|<1/200.              \tag{17}
\]
No saved value has been recomputed or replayed here.
Taylor's integral formula with (16), and
\(|E-7/20|\le7/50\), now give
\[
 \begin{split}
 \lambda(E)
 &>\frac{108}{125}-\frac1{200}\frac7{50}
                         -\frac{11}{2}\left(\frac7{50}\right)^2\\
 &=\frac{1511}{2000}>\frac34 .
 \end{split}                                                  \tag{18}
\]
Combining (10) and (18) proves, with the original absolute
action normalization,
\[
                     \boxed{\quad
                  \Re S(e)>\frac{1511}{2000}
                         \qquad(e\in\mathcal E).
                     \quad}                                 \tag{19}
\]

## 5. A paid full source sector, and the remaining bridge

The specified finite continuation is
\[
            C_N(e,w)=\sum_{l=0}^{N-1}
               \frac{e^{i\pi e l}e_l(w)}
                            {S_lG_N(Ne-l)} .                 \tag{20}
\]
[The uniform bridge tail theorem](research_mixed_endpoint_bridge_real_tails.md)
proves that every literal row with \(l/N\ge1/2\) has
rate less than \(67/105\), uniformly on the same strip
\(\mathcal E\), with all reciprocal zeros, carriers and
both parities retained. Equations (19)--(20) therefore give
the explicit own-action reserve
\[
       \frac{1511}{2000}-\frac{67}{105}
                  =\frac{4931}{42000}>\frac1{10}.             \tag{21}
\]
Thus the entire upper-half auxiliary source is exponentially
smaller than \(e^{NS(e)}\); after one common finite tolerance
and polynomial absorption, its relative gap may be \(1/20\).
The same conclusion holds for each fixed ordinary derivative
at complete color and on sufficiently small fixed complex
color/index neighborhoods, with the original polynomial
costs and an arbitrarily small additional allowance.
This follows from the zero-safe source bounds in the cited
tail theorem and compactness, not from the mere existence
of the critical branch.

The other real tails already reduce to the cuts
\(1/20\) and \(E-1/100\), but their comparison with (19)
or with the actual \(S(e)\) is not supplied here.
Neither are the horizontal aliases, whole vertical sides,
or the unweighted connectors to the actual auxiliary
critical height. Finally, no inclusion of the continued
outer cap path \(e(a)\) in \(\mathcal E\) has been proved
in this note. These are the remaining source obligations
before promoting the phase and tail results to a complete
endpoint packet or a whole cap contour theorem.
