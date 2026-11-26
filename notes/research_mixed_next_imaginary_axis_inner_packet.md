# The complete inner packet on the lower imaginary axis

Private finite-source theorem, 9 November 2026. The inner packet
extends along the whole compact axis \(u=-iK\), \(0\le K\le2/5\).
The outgoing factorial cut then lies on the right boundary.
A new incoming-cut estimate replaces the ineligible bound
\(|\cos u|\le1\). The stronger axis action floor permits a
shorter right-current path, with its final horizontal paid by
the full-period slit bound.

This proof retains the original finite source, both parity
cutoffs, all endpoint groups and Fourier corrections. No
mathematical numerical evaluation or frozen-source edit is used.

## 1. Statement and unchanged source

Use the original cubic branch, action, and amplitude:
\[
 t_*(u)=a_*(u)-iH_*(u),\qquad
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,
 \qquad S(u)=\Phi(t_*(u),u),\quad s=\Re S.
\tag{1}
\]
They have their original holomorphic branches on a neighborhood
of \(\mathcal U_+=\{0\le\Re u\le\pi/2,-1/2\le\Im u\le0\}\).
Keep exactly the two sources and normalization of
[the selected-curve assembly](research_mixed_next_selected_curve_inner_packet.md):
\(Q_N^{\rm sh}\) has its full first edge, second edge shortened to
\(U_N=\lfloor N/2\rfloor-1\), and the full inner Hermite trace;
\(Q_N^{\rm full}\) has both complete edges. In particular
\(C_{N,3}=q^{3(N-1)^2/4}\).

**Theorem.** Uniformly for \(u=-iK\), \(0\le K\le2/5\), at both
parities,
\[
 Q_N^\star(u)=C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                   \{1+O(N^{-1})\},
          \qquad \star\in\{{\rm sh},{\rm full}\}.
\tag{2}
\]
The original amplitude \(\mathcal A\) is bounded away from zero
on this compact axis. Both sources are consequently nonzero
there for all sufficiently large \(N\).

This is an axis theorem. It does not by itself assert a packet
on a prescribed negative lower corridor or control an outer
Fourier observation.

## 2. Axis action and first-height guards

Write \(c_*(u)=\cos(t_*(u)/2)=p+iq\). The original cubic
theorem gives \(p>3/4\), \(q>1/6\), \(0<a_*<\pi/2\),
and \(H_*<1\) throughout \(\mathcal U_+\).
For \(K>0\),
\[
 c_*(-iK)\tan(-iK/2)
       =q\tanh(K/2)-ip\tanh(K/2)
\]
lies in the open fourth quadrant. Its original principal
inverse hyperbolic sine has negative imaginary part.
Using the calibrated action derivative,
\[
 \frac{d}{dK}s(-iK)=
 -\frac1\pi\Im\operatorname{arsinh}
             \{c_*(-iK)\tan(-iK/2)\}>0 .
\tag{3}
\]
Thus the original complete action lower bound gives
\[
                  s(-iK)\ge M_3>9/5.
\tag{4}
\]
At \(K=0\) the derivative vanishes and the equality
\(s(0)=M_3\) has the original normalization.

The stronger first-height guard also holds:
\[
                         2/3<H_*(-iK)<1 .
\tag{5}
\]
Indeed write \(2c_*=x+ib\). The imaginary cubic equation is
\[
 (3b-2)x^2-b^3+2b^2-3b+2
                    =2\Im\cos(-iK/2)=0.
\]
For \(x>3/2\) its left side increases in \(b\in[1/3,2/3]\)
and is less than \(-1/4\) at \(b=1/2\). Hence \(b>1/2\).
The original inequalities
\(b<\sqrt2\sinh(H_*/2)\), \(\sqrt2<10/7\), and
\(\sinh(1/3)<18/53\) exclude \(H_*\le2/3\).

## 3. New complete incoming-cut guard

Consider the independent family
\[
 u=-iK,\quad0\le K\le2/5,\qquad
 t=a-iH,\quad\pi/2\le a\le2\pi/3,\quad1/10\le H\le1.
\tag{6}
\]
Put \(P=\cosh K\). The positive series gives
\[
                           1\le P<13/12.
\tag{7}
\]
Indeed the successive ratios after the quadratic term
in the hyperbolic cosine series are at most \(K^2/12\).
Consequently
\[
 \cosh K-1\le\frac{K^2}{2(1-K^2/12)}
                   \le\frac3{37}<\frac1{12}.
\]

For the original wire variable, the full force is
\[
 \mathfrak f(y)=
 \left|\frac{(\cos2\pi y+\cos t)(\cos2\pi y+P)}
                   {(1-\cos2\pi y)^2}\right|.
\tag{8}
\]
The incoming upper cut is
\(y=x+iH/(2\pi)\), \(x\ge1/2-a/(2\pi)\).
The outgoing upper cut has real starting coordinate \(1/2\),
so has no open interior segment in the wire half-strip.

On the incoming cut put
\[
 C=\cosh H,\quad q=-\cos2\pi x,\quad
 d=\cos a\in[-1/2,0],\quad d\le q\le1.
\]
As in the original cut proof,
\[
 \cos2\pi y=-Cq-i\sqrt{C^2-1}\sqrt{1-q^2},\qquad
 |1-\cos2\pi y|=C+q .
\tag{9}
\]
The incoming squared numerator increases with \(a\) through
this range. Its original endpoint bounds, valid for
\(1\le C<8/5\), are
\[
 \begin{array}{ll}
 q\le0:&
 O\le(q+1/2)^2(4C^2-1)/3,\\[2mm]
 q\ge0:&
 O\le q^2+A_Cq+B_C,\quad
 A_C=(8C^2-5)/3,\quad B_C=(4C^2-1)/12.
 \end{array}
\tag{10}
\]
These are the exact calculations (13)--(16) of
[the incoming-cut source](research_mixed_next_selected_right_edge_cut_guards.md);
they have no outgoing-angle hypothesis.

If \(q=-v\le0\), the other numerator is bounded by
\[
 |\cos2\pi y+P|
 \le|\cos2\pi y+1|+(P-1)
 \le\frac{13}{12}(C+v),
\]
since \(C+v\ge1\). The original rational maximization
\((1-5v)^2\ge0\) therefore gives
\[
                    \mathfrak f\le\frac{39}{32\sqrt3}<1.
\tag{11}
\]

If \(q\ge0\), its exact square satisfies
\[
 |\cos2\pi y+P|^2
       =C^2+q^2+P^2-1-2PCq
       \le C^2+q^2+\frac{25}{144}-2Cq.
\tag{12}
\]
Put \(d_1=25/144\). Subtracting the product of the bounds
in (10),(12) from the squared denominator gives
\[
\begin{split}
 &(C+q)^4-(q^2+A_Cq+B_C)(q^2-2Cq+C^2+d_1)\\
 &=(6C-A_C)q^3
  +(5C^2-d_1+2CA_C-B_C)q^2\\
 &\quad+\{C^2(4C-A_C)-d_1A_C+2CB_C\}q
       +C^4-B_C(C^2+d_1).
\end{split}
\tag{13}
\]
All four coefficients are positive on \(1\le C\le8/5\).
For the linear coefficient, the original concavity bound
\(4C-A_C\ge31/25\) and \(A_C\le129/25\) give the positive
lower bound \(31/25-43/48\). The cubic and quadratic
coefficients are positive from these same bounds and
\(B_C<C^2/3\). The constant is at least
\[
 \frac23C^4-\frac{25}{432}C^2
                         \ge\frac{263}{432}C^4.
\]
Since \((C+q)^4\le16C^4\), this proves
\[
                    \mathfrak f^2\le1-\frac{263}{6912}<1.
\tag{14}
\]
Equations (11),(14) retain the complete force at every
incoming-cut point, including its starting zero.
No bound \(|\cos u|\le1\) has been used.

## 4. Original saddle, upper paths and complete aliases

For (6), set \(A=\cos^2(t/2)\), \(B=\cosh^2(K/2)\),
\(D=A+B-AB\), \(W=AB/D\). The original incoming guards give
\[
 \Re A>1/10,\quad |A|<4/5,\quad |1-A|<21/20,\quad
 \Im A>0.
\]
Equation (7) yields \(1\le B<25/24\). In particular
\[
 |1-D|<7/160,\qquad
 \Re(1/W)=\Re(1/A)+1/B-1
                 >5/32-1/25=93/800,\qquad
 \Im(1/W)<0.
\tag{15}
\]
Thus \(W\) remains in a compact subset of the upper right
quadrant. The original simple wire saddle
\[
 y_*=\pi^{-1}\arctan\sqrt W,\qquad
 -F_{yy}(y_*)=\frac{2\pi D(1+W)^2}{W^{3/2}}
\tag{16}
\]
stays in the upper open half-strip and is nondegenerate.
Start at \(a=\pi/2,H=H_*(-iK)\), where the adopted positive
edge packet on all of \(\mathcal U_+\) fixes the logarithmic
charge. Vary \(H\), then \(a\). The force guards above
exclude a critical crossing of the sole interior cut.
Therefore \(F_y(y_*)=0\) and \(F(y_*)=\psi(t,-iK)\)
retain their original lifts and additive constants.

Here are all boundary facts required for the upper-path proof.
The envelope \(\mathcal V=\mathfrak b(y,t)+\mathfrak b(y,-iK)\)
is continuous and subharmonic, with the original positive
normal jump on the incoming cut and vanishing starting-zero
flux. The cut decreases horizontally by (11),(14).
Off the cut it is nonconstant harmonic.
On the real open wire, the outgoing quotient
\[
             \frac{\cos2\pi x+\cosh K}{1-\cos2\pi x}
\]
is positive real, with original imaginary logarithm zero.
The incoming quotient has original argument in \((0,\pi)\).
Thus \(\partial_v\mathcal V(x+i0)<0\); there is no bottom
local minimum.

On the left side the outgoing one-leg derivative is \(\pi\),
and the incoming one is positive. On the right side, the
zero-angle limit of the original one-leg formula is
\[
 \partial_v\mathfrak b(1/2+iv,-iK)=
 \begin{cases}0,&0<v<K/(2\pi),\\ \pi,&v>K/(2\pi).\end{cases}
\tag{17}
\]
The incoming leg has derivative in \((-\pi,0)\) before
its height and at least \(\pi\) afterwards. Consequently
the sum decreases up to \(\min(H,K)/(2\pi)\) and increases
afterwards. If \(H<K\), the incoming crossed derivative
is already positive while the outgoing derivative is zero.
If \(K<H\), the outgoing crossed derivative \(\pi\) exceeds
the magnitude of the incoming negative derivative.
Equal heights and \(K=0\) give the same connected-sublevel
conclusion by their one-sided limits. Its real endpoint is
\(e=(H+K)/2\), while the left endpoint is zero.

At large upper height
\[
                   \mathcal V(x+iv)=2\pi v-aH/(2\pi)+o(1).
\]
The original component/Jordan lemma now constructs an
unweighted upper path at rate
\(\max\{\Re\psi(t,-iK),e\}+\varepsilon\).
This application includes every boundary minimum and cut;
it uses the same simple saddle, not a new stationary point.
Compactness supplies finite path covers and uniform constants.

For completeness, the two penalized side rates are
\[
 \mathcal V(\pm iv)-2\pi v\le aH/(2\pi),\qquad
 \mathcal V(1/2\pm iv)-2\pi v\le e .
\tag{18}
\]
Their original sidewise formulas allow zero real angle.
The left reserve is
\[
                  e-aH/(2\pi)\ge H/6+K/2\ge1/60.
\]
Use wire heights \(+2,-2\) for the two complete alias
horizontals. The original complete dilogarithm remainder
is less than \(1/600\), since all its arguments have modulus
at most \(e^{1-4\pi}<1/10000\). Thus the same deep reserve
and endpoint collars as in
[the vertical source theorem](research_mixed_next_selected_right_edge_vertical_upper_envelope.md)
remain valid.

There is no change to the finite interpolation
\[
 T_N(y)=B_N(y,t)B_N(y,-iK),\qquad
 B_N(y,z)=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2}.
\tag{19}
\]
Its shifted real arguments retain the original fixed
margin in \((-1,1)\). Reciprocal reflection proves
holomorphy throughout \(0<\Re y<1/2\).
The original zero-safe factorial bounds control every
physical row \(0\le j\le U_N\), including both endpoint
groups and the actual odd last index.

In detail, choose the original midpoint cuts
\(\alpha_N,\gamma_N\) and a small fixed cap height \(h_c\).
Let \(\Gamma_\pm\) run left to right through heights \(\pm2\),
with their full endpoint columns. For \(\zeta=e^{2\pi iNy}\),
the exact formula is
\[
\begin{split}
 K_N^<(t,-iK)
  ={}&N\int_{\Gamma_+}\frac{T_N}{1-\zeta}\,dy
     +N\int_{\Gamma_-}\frac{T_N}{\zeta-1}\,dy\\
 &+N\int_{\gamma_N-ih_c}^{\gamma_N+ih_c}
                 \frac{T_N}{\zeta-1}\,dy
  -N\int_{\alpha_N-ih_c}^{\alpha_N+ih_c}
                 \frac{T_N}{\zeta-1}\,dy\\
 &+\sum_{j=0}^{\lfloor N\alpha\rfloor}T_N(j/N)
  +\sum_{j=\lceil N\gamma\rceil}^{U_N}T_N(j/N).
\end{split}
\tag{20}
\]
Split the first reciprocal as \(1+\zeta/(1-\zeta)\),
and move its entire unweighted integral to the upper path.
The added segments are exactly
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy
       +N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy .
\]
All caps and these two segments lie in the paid endpoint
collars. Midpoint cap reciprocals have modulus at most one.
Both remaining full aliases supply their exact
\(e^{-2\pi N|\Im y|}\) penalties. Polynomial factors are
absorbed in any fixed tolerance. Hence, uniformly on (6),
\[
 |K_N^<(t,-iK)|\le C_\tau
   \exp N\{\max(\Re\psi(t,-iK),(H+K)/2)+\tau\}.
\tag{21}
\]

## 5. The complete remaining inner current

The original one-current reduction was proved on all of
\(\mathcal U_+\). It is therefore already eligible on this
axis, with its full partial Gaussian, negative currents,
first-edge trace tail, physical normals, both endpoint
verticals and both parity central terms. Its only unpaid
current has the unchanged short-by-short integrand
\[
 g_N(t,u)=\sin t\,K_N^<(t,0)K_N^<(t,u)
                           e^{3iNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},
 \quad\eta=(-1)^{N-1},
\tag{22}
\]
and the scalar \(-N^2C_{N,3}/(\pi i)\).

Its lower-half-plane path can now be taken to be
\[
 \pi/2-iH_*
 \longrightarrow2\pi/3-iH_*
 \longrightarrow2\pi/3-i/10
 \longrightarrow5\pi/6-i/10.
\tag{23}
\]
This is an exact Cauchy replacement with the same endpoints.
There is no enclosed angular sampling pole. All its heights
are at least \(1/10\), so the full \(W_N\), not only a
chosen Fourier term, has rate \(-H\).

On the first segment, the geometric rate is the original
\(\Re\Phi\). The adopted horizontal concavity and positive
extension give a uniform gap from \(s(-iK)\), since
\[
 d_{\rm ax}=\pi/2-\max_{0\le K\le2/5}a_*(-iK)>0 .
\]
The endpoint-sector rate is
\[
 \Re\psi(a-iH,0)+\frac{H+K}{2}
                         +\frac{3aH}{2\pi}-H<33/20.
\tag{24}
\]
The proof of this last bound in the action-floor application
uses only \(a\le2\pi/3,H\le1,K\le2/5\), with \(H\ge2/3\);
it does not use an outgoing real angle or selected equation.
Equations (4),(21),(24) pay this whole segment.

For the vertical put \(t_0=2\pi/3-i/10\). The adopted
first-edge estimate, with its written secant bounds, is
\[
                 2\Re\psi(t_0,0)<19/12+1/300.
\tag{25}
\]
The original return at outgoing parameter \(-ik\) remains
principal for \(0\le k\le K\); its imaginary part lies
between \(-\pi/2\) and zero. Integrating \(\psi_u\) gives
\[
       \Re\psi(t_0,-iK)\le\Re\psi(t_0,0)+K/2 .
\tag{26}
\]
The crossing-plus-charge rate vanishes at this first real
angle. Thus
\[
                 \Re\Phi(t_0,-iK)<134/75<9/5.
\tag{27}
\]
The original positive-horizontal phase theorem has
\(\Re\Phi_{tt}<0\) through \(a=2\pi/3\), uniformly for
the entire outgoing \(\mathcal U_+\). Consequently its
vertical real part is convex. Its upper endpoint is
below \(s\) by the horizontal descent; its lower endpoint
has the fixed gap \(1/75\) in (27). The whole geometric
vertical is paid. The endpoint-sector expression on this
vertical equals
\(\Re\psi(2\pi/3-iH,0)+(H+K)/2\).
It increases with \(H\), since the first-edge height
derivative is positive. Its maximum is the already paid
upper endpoint (24). This pays the entire vertical
using the complete estimate (21).

Finally use the complete-period slit bound on the last
segment. It gives the actual second short edge rate
\(\Re\psi(t,0)+K/2\), at both parities, for every
\(2\pi/3\le\Re t\le5\pi/6\) at height \(1/10\).
Together with the first short edge and full multiplier,
the rate is
\[
 R(a)=2\Re\psi(a-i/10,0)+K/2+3a/(20\pi)-1/10.
\tag{28}
\]
At \(a=2\pi/3\), (25) gives \(R<134/75\). The adopted
return lower bound \(\Re\operatorname{arsinh}\tan((a-i/10)/2)>19/20\)
on this interval gives
\[
                            R'(a)<-7/(4\pi)<0.
\tag{29}
\]
Thus the entire final horizontal is below \(s\) by \(1/75\).

Choose the fixed tolerances in the two slit estimates
and (21) below these uniform gaps. The original \(N^2\)
scalar, lengths and bounded factors change only the
polynomial prefactor. There is consequently an
\(\varepsilon_{\rm ax}>0\), independent of \(K,N\) and
parity, such that the whole current (23) is bounded by
\(C\exp N(s(-iK)-\varepsilon_{\rm ax})\).
The unchanged one-current identity and its nonzero Gaussian
coefficient now prove (2) for \(Q_N^{\rm sh}\).

The independently proved outgoing-tail restoration gives
\[
 |Q_N^{\rm full}(-iK)-Q_N^{\rm sh}(-iK)|
                 \le CN^A e^{47N/30}.
\tag{30}
\]
The action floor (4) leaves a gap greater than \(7/30\).
Adding the whole finite difference proves (2) for the
full source. No error term has been inserted into an
unestimated cancelling outer sum.

## Frozen source bindings and scope

- Original full single-three action lower bound:
  7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c.
- Original whole cubic and calibrated derivatives:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Original single-current identity:
  2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421.
- Exact selected-curve source definitions:
  e3bc75e93e1c1834faa920ff2f4ef0711c8f6cc7906b6c0c5b59bbadc86f57b7.
- Incoming-cut calculation:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Complete upper envelope and both side limits:
  c7ea7e57bfcb41d7fcbc65202e281181576c76710dc5c5a00d6e436200cbb699.
- Complete vertical finite interpolation and aliases:
  2498045028562d23a06990b9175d9799177c0e2896c2d5eaf0e51d0d082c31d6.
- Original positive horizontal phase extension:
  a643c0878b4a4c23010f3d15731e72907c55cb0f19639b9dba922b57235f4e1c.
- First-edge low-height estimate:
  5813ddfa3f16e81c7907bbf8e11f6be0d07d30e0e71a74f5845d889aa1a4ac85.
- Endpoint-sector ceiling:
  492ae47bfcaa02198c0e819ef97cb9e7afb7c066d559a84373031091612b2c53.
- Whole-period first-short slit theorem:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Full outgoing-tail restoration:
  8b30fb2a8258d49fd8c162d5822c4652129ffc5a39ee77019e1b00aa2db7596e.

The result supplies an actual complete inner packet on the
central axis. Extending it to a specified negative lower
corridor still requires source estimates there; neither
evenness nor a Schwarz-reflection argument is asserted.

