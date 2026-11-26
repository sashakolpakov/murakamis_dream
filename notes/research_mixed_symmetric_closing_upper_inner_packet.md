# The complete inner-three source on the upper outgoing rectangle

Private finite-source proof, 9 November 2026. The original complete
inner-three packet extends to the upper outgoing rectangle. A variable
diagonal taper pays both the saddle and endpoint sectors of the
opposite-height high edge. An all-real incoming upper bound then pays
the negative middle part of the original outer closing current.

Every original edge row, Hermite normal, trace charge, alias and cap
is retained. No mathematical numerical evaluation, saved-value arithmetic,
import, compilation or frozen-source edit is used.

## 1. The original source and conclusion

Retain the complete ordinary kernels, crossing and full Hermite trace:
\[
 D=N-1,\quad U=\lfloor N/2\rfloor-1,\qquad
 C_{N,3}=e^{3\pi iD^2/(4N)},\qquad
 \phi_N(f)=(-1)^DN^2[x^D]\operatorname{rem}_{2T_N(x/2)+2}f,
\]
\[
 \mathcal K_N(w,x)=\sum_{j=0}^{D}e_j(w)e_j(x),\quad
 \mathcal K_N^<(w,x)=\sum_{j=0}^{U}e_j(w)e_j(x),
\]
\[
 Q_N(w,u)=\phi_N[R_N^3\mathcal K_N(w,x)
                           \mathcal K_N(x,-2\cos u)] .
 \tag{1}
\]
The outgoing set is
\[
 \mathcal V^\uparrow
   =\{\beta+iK:0\le\beta\le\pi/2,\ 0\le K\le7/10\}.
 \tag{2}
\]
The phase \(S(u)\), its constant, and the critical point
\(t_*(u)=a_*(u)-iH(u)\) are the original ones in the taller strip
theorem:
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it,\quad
 \Phi_t(t_*(u),u)=0,\quad S(u)=\Phi(t_*(u),u).
 \tag{3}
\]
In particular the crossing in (1) remains \(+3\).

**Theorem.** Uniformly on (2), at both level parities, the complete
finite source satisfies
\[
 Q_N(-2,u)=C_{N,3}N^{-3/2}A(u)e^{NS(u)}
                                  (1+O(N^{-1})),
 \tag{4}
\]
with the original nonzero coefficient
\[
 A(u)=\frac{i\sqrt{2\pi}}{\pi}
 \frac{\sin t_*(u)\,a_e(t_*(u),0)a_e(t_*(u),u)}
                         {\sqrt{-\Phi_{tt}(t_*(u),u)}}.
 \tag{5}
\]
The square root has the original increasing-horizontal orientation.
A second conclusion, useful for the outer negative current,
is the complete all-real-incoming upper bound, for every fixed
\(\tau>0\),
\[
 \sup_{w\in[-2,2]}|Q_N(w,u)|\le C_\tau e^{N(\Re S(u)+\tau)}.
 \tag{6}
\]
A fixed sufficiently small complex neighborhood of the real incoming
interval costs an arbitrarily prescribed positive rate allowance.
This does not use conjugation of the complete \(+3\) source.

## 2. Height and action on the upper rectangle

Write \(c=\cos(t_*/2)=p+iq\), \(v=2c=x+ib\), and
\(C=\cos(u/2)\). The adopted taller strip theorem gives
\[
 x>3/2,\quad1/3<b<2/3,\quad 0<a_*<\pi/2,\quad0<H<1,
 \qquad |\Im C|<2/7,
\]
\[
 2\Im C=(3b-2)x^2-b^3+2b^2-3b+2 .
 \tag{7}
\]
At \(b=2/5\), the right side of (7) is
\[
 -4x^2/5+132/125<-93/125<-4/7.
 \tag{8}
\]
The final comparison is \(651>500\). At fixed \(x>3/2\),
the derivative of the right side of (7) with respect to \(b\)
is \(3x^2-3b^2+4b-3>19/4\) on \([1/3,2/3]\).
Since \(2\Im C>-4/7\), this proves \(b>2/5\) for the
original root. If \(H\le1/2\), the original identity
and positive series imply
\[
 b=2\sin(a_*/2)\sinh(H/2)
 <\sqrt2\sinh(1/4)
 <(10/7)(24/95)=48/133<2/5.
 \tag{9}
\]
Here \(\sinh x\le x/(1-x^2/6)\) at \(x=1/4\).
This contradiction proves
\[
                         1/2<H(u)<1.
 \tag{10}
\]

The original outgoing derivative is
\[
 S'(u)=-\pi^{-1}\operatorname{arsinh}
                      \{c(u)\tan(u/2)\}.
 \tag{11}
\]
The taller strip proof guards the principal return by
\(|\Im(c\tan(u/2))|<95/96\). On the upper rectangle, \(c\) is
in the first quadrant, and \(\tan((\beta+iK)/2)\) has nonnegative
real and imaginary parts. Their product has positive imaginary
part except at \(u=0\). The continued principal return has the
same imaginary sign. Hence
\[
 \partial_K\Re S(\beta+iK)
       =\pi^{-1}\Im\operatorname{arsinh}
                         \{c(\beta+iK)\tan((\beta+iK)/2)\}\ge0.
 \tag{12}
\]
The exact real-path bound and original \(M_3>46/25\) thus give
\[
 s_+(u):=\Re S(u)>
 \frac{46}{25}-D_{\rm real}(\beta),\qquad
 D_{\rm real}(\beta)=-\frac{32}{17\pi}\log\cos(\beta/2).
 \tag{13}
\]
In particular, with the unchanged rational bound
\(D_{\rm real}(\pi/2)<448/2125\),
\[
                         s_+(u)>3462/2125>321/200.
 \tag{14}
\]
The last cleared comparison is \(692400>682125\).
No downward-height loss is subtracted in (13).

## 3. The central source, including its negative part and center

The exact Newton coefficients are real. Therefore
\[
 K_N^<(t,u)=\overline{K_N^<(\bar t,\bar u)} .
 \tag{15}
\]
For \(u\) in (2), \(\bar u\) is in the adopted taller lower
rectangle. For every fixed \(a_L>0\), both first angles
\(a\pm iH\), \(a_L\le a\le\pi/2\), belong to the independent
signed first-angle domain of the taller mixed-edge theorem.
Conjugating that edge theorem gives the original relative
packet for \(K_N^<(a-iH,\beta+iK)\). Exact evenness in the
first angle supplies the corresponding negative first angles.
The real-angle calibration of the primitive, followed by
continuation in the connected height box, identifies the
phase in (15) with \(\psi(t,u)\) in (3). This operation is
performed only on the bare edge. It does not conjugate the
crossing in (1).

The same signed primitive has
\[
 \Phi_{tt}(t,u)=
 -\frac1{2\pi}\left\{\frac1c+
                  \frac{C}{c\sqrt{D_0}}\right\}
                              +\frac{3i}{2\pi},\quad
 c=\cos(t/2),\ C=\cos(u/2),\
 D_0=c^2+C^2-c^2C^2.
 \tag{16}
\]
On \(|\Re t|\le\pi/2,\ |\Im t|\le1\), the taller mixed
source's absolute argument bounds apply at either sign of
\(\arg C\). They give positive real part for the second
ratio in (16), and \(\Re(1/c)>1/2\). Consequently
\[
 \Re\Phi_{tt}<-1/(4\pi),\qquad
 \Re\Phi(a-iH(u),u)
        \le s_+(u)-\frac{(a-a_*(u))^2}{8\pi}.
 \tag{17}
\]
The complete first edge has its original source bound at
\(\Re\psi(t,0)\), and the shortened first edge has the same
bound. This retains the full original odd middle row in
their difference.

For a fixed positive small first-angle cutoff, (15)--(17)
pay every central portion separated from \(t_*(u)\).
Across first angle zero use the exact polynomial center
argument from the taller mixed-edge theorem, Section 7:
the product of two shortened edges has spectral degree
\(2U<N\), and after \(x=\tan(a/2)\) its clearing polynomial
has degree \(4U<2N\). Its continuation cost is therefore
no larger than the original allowed \(3N\) cost.
Choose the real interval and its smaller center cutoff
using the fixed positive minimum of \(a_*(u)\). The
complete \(W_N\) penalty cancels the restored \(NH\)
term as in that proof. This is a finite polynomial
bound at the center, not a packet at first angle zero.

Near \(t_*(u)\), use (15) and the original full first-edge
packet, or its exponentially equivalent shortened version.
Their nonzero local coefficients and the increasing
horizontal Gaussian give exactly (5), with the original
\(C_{N,3}N^{-3/2}\). The other Fourier charges of \(W_N\)
are exponentially lower because of (10).

## 4. Two Hessian signs valid for both outgoing height signs

For the right first-angle part let
\[
 0<a\le2\pi/3,\quad 1/10\le H\le1,\quad
 t=a-iH,\quad u\in\mathcal V^\uparrow .
 \tag{18}
\]
Write \(A=c^2,\ B=C^2,\ D_0=A+B-AB\), as in (16).
The original elementary bounds give
\[
 |1-A|<21/20,\quad |1-B|<13/20,\quad
 |1-D_0|<273/400<1/\sqrt2 ,
\]
\[
 0<\arg c<\pi/4,\quad -7/20<\arg C\le0,\quad
 |\arg\sqrt{D_0}|<\pi/8,\quad
 \Re(1/c)>7/8 .
 \tag{19}
\]
Because \(7/20<\pi/8\), the ratio \(C/(c\sqrt{D_0})\)
has positive real part. Its branch is the original one:
\(D_0\) remains in the displayed disk about one and the
source primitives agree with the central primitive.
Thus \(\Re\Phi_{tt}<-1/(4\pi)\).

Here is a sign-independent modulus estimate for the same
ratio. Put \(p_A=|A|\). One has \(p_A\ge1/4\),
\(|B|\ge1/2\), and \(|B|<23/20\).
If \(p_A\ge1/2\), then (19) gives
\[
 \left|\frac{C}{c\sqrt{D_0}}\right|^2
 =\frac{|B|}{|A||D_0|}
 <\frac{920}{127}<9 .
 \tag{20}
\]
If \(1/4\le p_A\le1/2\), use \(D_0=B+A(1-B)\) instead:
\[
 \frac{p_A|D_0|}{|B|}
 >p_A-\frac{13}{10}p_A^2
 \ge\min\{27/160,7/40\}=27/160>1/9.
 \tag{21}
\]
The middle inequality is concavity on the indicated interval.
Equations (20)--(21) prove \(|C/(c\sqrt{D_0})|<3\).
Since \(\Im(1/c)<0\), (16) now yields
\[
                         \Im\Phi_{tt}>0.
 \tag{22}
\]
In particular the old same-sign lower bound
\(\Re D_0>11/20\) is not being imported into the
opposite-height family.

## 5. A variable-slope diagonal and both attached sectors

For \(H=H(u)\) define
\[
 r(u)=\min\{1,\ 6(H-1/10)/\pi\},\quad
 h_1=H-r\pi/6\ge1/10 .
 \tag{23}
\]
By (10), \(r>1/2\). If \(H\ge2/3\), then \(r=1\).
Take the rightward diagonal and subsequent upward vertical
\[
 \begin{split}
 t(a)&=a-i\{H-r(a-\pi/2)\},
                       &&\pi/2\le a\le2\pi/3,\\
 t&=2\pi/3-ih,          &&h_1\ge h\ge1/10 .
 \end{split}
 \tag{24}
\]
A zero-length second segment is allowed.

Set \(R(a,h)=\Re\Phi(a-ih,u)\), and retain the literal endpoint
sector
\[
 E(a,h)=\Re\psi(a-ih,0)+(h+K)/2+3ah/(2\pi)-h.
 \tag{25}
\]
Let \(d=\pi/2-\max_{\mathcal V^\uparrow}a_*(u)>0\).
By (17),
\[
 R(\pi/2,H)\le s_+-d^2/(8\pi).
 \tag{26}
\]
The mixed endpoint lemma, conjugated as an edge statement,
also gives
\[
 E(\pi/2,H)<R(\pi/2,H)-1/400.
 \tag{27}
\]
Horizontal integration of both Hessian signs from \(a_*\)
shows \(\Re\Phi_t(\pi/2-iH,u)<0\) and
\(\Im\Phi_t(\pi/2-iH,u)>0\).
Consequently the initial diagonal derivative of \(R\) is
negative. Its second derivative is
\[
 \Re\{(1+ir)^2\Phi_{tt}\}
   =(1-r^2)\Re\Phi_{tt}-2r\Im\Phi_{tt}<0.
 \tag{28}
\]
Thus the geometric sector decreases along the whole diagonal.

For the endpoint sector put
\(r_0(t)=\operatorname{arsinh}\tan(t/2)\), on the original branch.
At \(a=\pi/2\) its derivative along (24) is
\[
 E'_D=\frac{3H/2-\Re r_0+r\Im r_0}{\pi}-r/4.
 \tag{29}
\]
This expression decreases with \(r\), since \(\Im r_0<0\).
If \(H\le2/3\), the function
\(\Re r_0-(1/2)\Im r_0\) increases from
\(\operatorname{arsinh}1>3/4\). Indeed its height derivative is
\[
 \tfrac12\{\Im\sec(t/2)+(1/2)\Re\sec(t/2)\}>0,
\]
because \(\tan(\arg\cos(t/2))=\tanh(H/2)<1/3<1/2\).
Using \(r>1/2\) in (29) gives
\(E'_D<1/(4\pi)-1/8<0\).
If \(H\ge2/3\), then \(r=1\), and the original diagonal
argument gives \(E'_D<0\): here
\(\Re r_0-\Im r_0>\operatorname{arsinh}1>3/4\) and \(H<1\).

The holomorphic function whose real part is (25) has second
derivative \(-\sec(t/2)/(2\pi)+3i/(2\pi)\).
Its real part is negative and its imaginary part is positive.
Equation (28) with that function proves \(E''_D<0\).
Both attached sectors therefore decrease along the diagonal.

## 6. The low endpoint from a genuine finite-source comparison

The adopted
[opposite-height high-edge theorem](research_mixed_symmetric_closing_opposite_height_high_edge.md)
provides the complete bound
\[
 |K_N^<(t,u)|\le C_\tau
 e^{N(\max\{\Re\psi(t,u),(h+K)/2\}+\tau)}
 \tag{30}
\]
on (18) with \(\pi/2\le a\le2\pi/3\), with every endpoint
group, alias and cap.
It also gives the original nonzero local edge Gaussian
on compact subsets where
\(\Re\psi(t,u)>(h+K)/2\).
This relative conclusion, not merely its upper estimate, licenses
the following action comparison.

Let \(t_0=2\pi/3-i/10\). At each fixed \(u\), if
\(\Re\psi(t_0,u)>(1/10+K)/2\), this nonzero edge asymptotic
and the exact Cauchy--Schwarz inequality for the same finite
sum force
\[
 \Re\psi(t_0,u)\le m(2\pi/3,1/10)+m(\beta,K).
 \tag{31}
\]
Indeed the latter finite upper bound is the complete Newton
row estimate (8) of the low-horizontal theorem; taking
\(N^{-1}\log|\cdot|\) in the nonzero packet proves (31).
If the strict hypothesis fails, the geometric attached
rate is already no larger than the endpoint sector.

The low-horizontal proof retains
\[
 \mathcal R(t_0,u)
 <\frac{39}{20}-\frac{1171}{1800\pi}
                       -\frac{1-\cos\beta}{2\pi}.
 \tag{32}
\]
Its modulus estimates are unchanged when the outgoing
height is reversed. Equations (13) and (32), with the
exact real-loss comparison in that proof, give a gap
strictly greater than its already proved \(1/50\);
the downward debit \(2/(27\pi)\) is absent here.
The endpoint sector at \(t_0\) satisfies
\[
 E(2\pi/3,1/10)
 =\Re\psi(t_0,0)+1/20+K/2
 <47/60+1/20+7/20=71/60<s_+-1/50.
 \tag{33}
\]
Therefore, by the two cases preceding (31),
\[
                         R(2\pi/3,1/10)<s_+-1/50.
 \tag{34}
\]
This conclusion uses a nonzero finite-edge statement
where needed, not an inference from a formal critical value.

Along the vertical in (24), \(R_{hh}=-\Re\Phi_{tt}>0\).
Its two endpoints are paid by (26),(28) and (34);
convexity pays the whole vertical.
At real part \(2\pi/3\), the function \(E\) increases
with height, so its largest value is the already paid
diagonal endpoint. The first-short slit source, (30)
and the exact \(W_N\) now pay the entire high and vertical
current with a fixed gap. The variable slope and all
path lengths remain uniformly bounded.

## 7. Every other original current

For completeness the exact two-short trace is
\[
 Q_N^{<<}(-2,u)
 =-\frac{N^2C_{N,3}}{\pi i}\int_{\Gamma_N}
          \sin t\,K_N^<(t,0)K_N^<(t,u)e^{3iNt^2/(4\pi)}
          \frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}\,dt
       +E_N^{\rm far}(u),
 \tag{35}
\]
where \(\eta_N=(-1)^{N-1}\).
The taller fixed-low-remainder proof constructs the midpoint
ends
\[
 \Theta_N=\pi-2\pi\lfloor N/4000\rfloor/N,\qquad
 e^{iN\Theta_N}=-\eta_N,
\]
with a fixed sufficiently small \(h_c>0\), and proves all removed samples,
their normals and the full endpoint currents at a rate
below \(321/200-1/20\). Its estimates depend only on
\(|\Im u|\) and the exact degree \(U\); they apply unchanged
on (2), with (14). The odd simple node remains in (35).

The whole left inner path is
\[
 -\Theta_N-ih_c\longrightarrow-\Theta_N-iH
                         \longrightarrow-\pi/2-iH.
\]
The original slit bound, evenness and real edge coefficients
give its horizontal rate
\[
 E_{\rm left}(a,u)=2\Re\psi(a-iH,0)+K/2-H-3aH/(2\pi),
 \quad a\ge\pi/2,
 \tag{36}
\]
which decreases with \(a\).
At \(t_R=\pi/2-iH\), the real outgoing debit is less
than \(79/375\), as in the original left comparison.
Moving that outgoing argument upwards increases
\(\Re\psi(t_R,u)\): the half-cosine and the upper
half-tangent are in the first quadrant, and the original
principal return has positive imaginary part.
Thus the lower-outgoing debit \(HK/(2\pi)\) is absent.
The central concavity and (10) give
\[
 s_+-E_{\rm left}(\pi/2,u)
 >3H/2-K/2-79/375
 >3/4-7/20-79/375=71/375>1/10.
 \tag{37}
\]
The far left vertical has rate less than
\(1/100+K/2\le9/25\), by the exact half-grid denominator
and the same height derivative as in the fixed-low source.
All original factors and both orientations are retained.

The low horizontal from \(2\pi/3-i/10\) to \(5\pi/6-i/10\)
has the absolute row proof of the low-horizontal theorem.
Its input depends only on \(|K|\); (13) strengthens
its action comparison. It retains its gap \(1/100\).

The right far path from \(5\pi/6-i/10\) to
\(\Theta_N-i/10\) and then to \(\Theta_N-ih_c\) has the
same slit rate \(19/12+2\tau\) as before.
The floor (14) is stronger than the \(321/200\) floor
used there, so its gap \(1/50\) is unchanged.

Concatenating these paths, the central horizontal and
(24) preserves the exact finite current in the lower
half-plane without added residues. The two edge
deletions are restored by the all-integer-power theorem:
their complete difference has rate at most
\[
 2b_2+K/2+K^2/(4\pi)<623/400 .
 \tag{38}
\]
This is an all-real-angle, both-parity statement for
the full Hermite contraction. Equation (14) leaves
the same fixed \(1/25\) restoration gap.
The central Gaussian then gives (4)--(5).

## 8. Real incoming colors and a fixed ordinary neighborhood

For \(w\in[-2,2]\), replace only the first shortened factor
in (35) by \(\mathcal K_N^<(w,-2\cos t)\).
The complete outside-period slit theorem bounds it at
\(\Re\psi(t,0)+\tau\), uniformly in all real \(w\).
This is precisely the first-factor rate in every
remote estimate above. It also gives the upper bound
on the central local portion; no relative packet at
that arbitrary real incoming color is required.
The exact center polynomial argument is uniform in
these coefficients. Both edge-deletion estimates
hold on the whole real incoming interval.
Take each slit allowance smaller than both the prescribed
\(\tau\) and the previously fixed remote gaps, and absorb
the polynomial factors in the remaining allowance. This
proves (6), without claiming a polynomial error for the
slit normal-family theorem itself.

For fixed outgoing \(u\), the exact function in (1)
has ordinary incoming degree at most \(D\).
Filled Bernstein ellipses of sufficiently small fixed
parameter therefore extend (6) to a fixed complex
neighborhood of \([-2,2]\) with any prescribed
positive rate allowance. Cauchy's formula on a
smaller neighborhood retains every fixed incoming
ordinary derivative at that same allowed rate.
This continuation is of a proved all-real bound
for the original finite polynomial; it is not a
continuation of an error known only at \(w=-2\).

## 9. The remaining negative middle outer current

Retain the exact original outer integrand
\[
 G_N(u;\mathbf w)=\sin u\,Q_N(w_L,u)Q_N(w_R,u)e^{iNu^2/\pi},
 \qquad W_N(u)=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2}.
 \tag{39}
\]
Let \(u_g=\beta_g-iK_g\) be the actual geometric point and
\(M_g=\Re\Xi(u_g)\), with
\(\beta_g>2\pi/5\), \(17/30<K_g<7/10\).
The exact finite polynomial is even in its angular argument:
\(Q_N(w,-a-iK_g)=Q_N(w,a+iK_g)\).
The original stationary action is also even: its derivative
in (11) is odd because the original cubic root depends
holomorphically on \(\cos(u/2)\). The equality \(S(-u)=S(u)\)
is calibrated at \(u=0\), retaining the unchanged complete constant
\(S(0)\).
No complex conjugation of the crossing is used in either identity.

The adopted symmetric-strip curvature bound gives
\[
 \Re\Xi(-a-iK_g)
 \le M_g-\frac{(a+\beta_g)^2}{32\pi}
 < M_g-\frac\pi{200},\qquad0\le a\le\pi/2.
 \tag{40}
\]
Choose the allowance in the ordinary-neighborhood version
of (6) to be \(1/2000\) for each of the two inner factors.
On the literal negative middle segment
\([-\pi/2-iK_g,-\eta-iK_g]\), (39), the exact denominator,
and (40) then give the absolute rate at most
\[
 M_g-\pi/200+1/1000.
\]
The sine, bounded path length and original \(N^2/\pi\)
cost only a polynomial. Spend a further \(1/1000\)
on it. Since \(\pi>3\), the remaining gap exceeds
\(3/200-1/500=13/1000>1/100\).
Thus this entire middle current has a fixed \(1/100\)
gap on a fixed incoming bidisk. All fixed incoming
ordinary derivatives obey the same estimate on a
smaller bidisk.

The adopted far-left connection theorem pays the
remaining deep vertical and negative horizontal
from the left midpoint endpoint to \(-\pi/2-iK_g\)
with gap \(1/20\). Combining these exact paths pays
the whole left connector in the original two-current
assembly, at a possibly smaller fixed gap.
The right outer connector and the general
short-partial-filling statement remain separate.

## Source bindings

- Taller phase: fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Taller mixed edge: 01630dd45f907e7d116fc8d51fed0ef00e13176f379b5ce1ab0186403cd1a94c.
- Original low/remaining inventory: 03accd56435b7c00be36b89a5e2ffcee70ae84027ad918a6b3b1dca204825ab0.
- Original diagonal taper: 7ba93b34b12765ebdfec7853ffc1e7e77bc370e07770c9088f59e538785af908.
- Complete low row norm: 0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
- Complete first-short slit: efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Both complete deletions: f7abba0175c558ee9ca7f94799f9cd4d58adc249fea3f6b8c425e55a8136da66.
- Opposite-height high-edge source:
  [complete opposite-height envelope](research_mixed_symmetric_closing_opposite_height_high_edge.md),
  19aa75ce4c6c8b461e55295da4ce51c67bf4ee83d4550318773b01a302bdc74d.
- Original symmetric horizontal concavity: f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b.
- Complete far-left connection: d02646e7422138c265de9ed1e16749590a8cb2f808b9cf15f30e584627aa6184.
- Exact original outer two-current assembly:
  [the two remaining currents](research_mixed_symmetric_closing_two_remaining_currents.md),
  15c28d0004bfcdebd26e55dfe48419aa54d14c563c95e33e1d32ef5b1ac6cad8.

