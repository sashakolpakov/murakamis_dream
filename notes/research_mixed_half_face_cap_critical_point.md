# The original first-cap critical point at the incoming half face

Research deduction, 7 November 2026. At the exact incoming argument
\(X=-1\), the type-three first cap has a uniquely specified critical
point inside the already proved endpoint-coefficient rectangle.
Its original logarithmic equation has zero lift. The retained
horizontal private integral therefore has a nonzero Gaussian
contribution with its original normalization.

This is not an asymptotic for the whole cap or a comparison with the
selected next-source action. The real cut currents, aliases and
physical tails remain. No numerical evaluation is used.

## 1. The finite source and its original phase

Put \(D=N-1\), \(q=e^{\pi i/N}\), \(r=q^{-2}\), and
\[
 P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j,\qquad
 U_{0,N}(w,X)=\sum_{j=0}^D H_N(w,r^{-j})\frac{p_j(X)}{P_j}.
 \tag{1}
\]
Here \(H_N\) is the whole original ordinary endpoint polynomial.
The exact retained private-row interpolation in
[the complete-current reduction, equation (4)](research_mixed_cap_outer_contour_reduction.md)
is
\[
 \mathscr A_N(e,a,w)
  =D_N(e)^{-1}\mathcal C_N(e,w)
      \frac{\widehat P_N(N(e+a))}{\widehat P_N(Na)},
 \qquad X=e^{-2\pi ia}.
 \tag{2}
\]
At physical \(e=j/N\), (2) is the summand of (1). The entire
endpoint coefficient \(\mathcal C_N\), its actual factorial
continuation, and its normalization are retained.

Let \(J'(z)=\operatorname{Log}(2\sin\pi z)\) be the original strip
branch, and write \(S(e,w)\) for the original endpoint action. At
complete color \(w=-2\),
\[
 \begin{split}
 S(e)&=F(e,u_c(e)),\\
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 \Psi(e,a,w)&=S(e,w)+J(e+a)-J(a)-i\pi ea .
 \end{split}
 \tag{3}
\]
These are precisely the actions in
[the full-index endpoint theorem](research_complete_boundary_full_index_interval.md)
and [the complete first-cap packet](research_mixed_complete_first_cap_packet.md).
The endpoint packet is available on a neighborhood of
\[
 E_c=[27/100,49/100]+i[-11/200,1/25].
 \tag{4}
\]
No first-cap outgoing-domain theorem is being extended to \(a=1/2\)
by assumption. Only the actual endpoint packet and the row
interpolation (2) are used below.

For comparison, the neighboring conditional source has the exact
duplication formula
\[
 C_{1,N}(-1,Y)=
    \sum_{j=0}^D
       \frac{(-1)^j(r^2;r^2)_j\,p_j(Y)}{P_j^4}.
 \tag{5}
\]
This follows from \(p_j(-1)=(r^2;r^2)_j/P_j\). For even \(N\),
all terms with \(j\ge N/2\) are zero. For odd \(N\), none of
these numerator factors vanishes before \(j=N\). Formula (5)
therefore does not license deleting the odd-level upper rows.
The first-cap deduction below holds at both parities and makes no
asymptotic claim for (5).

## 2. The rational critical equation and the original branch

Use variables distinct from the ordinary color:
\[
                    p=e^{2\pi ie},\qquad
                    \omega=e^{2\pi iu_c(e)} .
 \tag{6}
\]
The original endpoint equation gives
\[
 p=\frac{5\omega^2-2\omega+1}{(\omega+1)^2},\qquad
 (p-5)\omega^2+2(p+1)\omega+(p-1)=0.
 \tag{7}
\]
It is the same endpoint rational relation used in
[the exact curvature formulas](research_mixed_pair_curvature_composition.md).
The endpoint envelope derivative is
\(S'(e)=-J'(e-u_c(e))+i\pi u_c(e)\). Consequently
\[
 \exp\Psi_e(e,a,-2)
      =\frac{\omega(p-X)}{p-\omega},
                   \qquad X=e^{-2\pi ia}.
 \tag{8}
\]
For example the sine ratio in this calculation is
\[
 \frac{\sin\pi(e+a)}{\sin\pi(e-u)}
       e^{i\pi(u-a)}
         =\frac{\omega(p-X)}{p-\omega}.
 \tag{9}
\]
This retains the original chirp.

The rational stationary equation obtained from (8) is
\[
 \begin{split}
 \mathfrak p_X(\omega)
   &:=(6-X)\omega^3-(5+2X)\omega^2+(4-X)\omega-1=0,\\
 X&=\frac{6\omega^3-5\omega^2+4\omega-1}
                    {\omega(\omega+1)^2}.
 \end{split}
 \tag{10}
\]
These equations alone do not choose a logarithmic branch or prove
source dominance. At \(a=1/2\), \(X=-1\), they become
\[
 f(\omega):=7\omega^3-3\omega^2+5\omega-1=0,\qquad
                         p=\frac{2\omega}{1-\omega}.
 \tag{11}
\]

The branch in (7) can be identified without approximating a root.
For every \(\Im p>0\), its quadratic has exactly one root with
positive imaginary part. Its discriminant is \(16(2p-1)\),
which never vanishes there. A real root \(\omega\) would give a
real value of \(p\) in (7); \(\omega=-1\) is not a root, and
the leading coefficient cannot vanish in the open upper half-plane.
Hence roots cannot cross the real line or escape to infinity
while \(p\) moves there. At \(p=1+i\varepsilon\), the two roots are
\[
 1+i\varepsilon+O(\varepsilon^2),\qquad
              -i\varepsilon/4+O(\varepsilon^2).
 \tag{12}
\]
Their signs establish the assertion on the connected upper half-plane.
The upper root is the original endpoint branch: as positive real
\(e\) tends to zero, \(u_c(e)\to0\) and the corresponding
\(\omega\to1\) on precisely this branch. Uniqueness then identifies
its continuation throughout the half strip \(0<\Re e<1/2\),
including (4).

The real cubic in (11) has exactly one real root \(\alpha\), since
\[
 f'(t)=21(t-1/7)^2+32/7>0,\qquad
 f(1/5)=-8/125<0,\quad f(1/4)=11/64>0 .
 \tag{13}
\]
Thus \(1/5<\alpha<1/4\). Let \(\omega_+\) be its nonreal
upper root. The two remaining roots form a nonreal conjugate pair:
a second real root is impossible, and a repeated nonreal root
would force its conjugate to have the same multiplicity.
Writing \(\omega_+=\sigma+i\tau\), Vieta's formulas give
\[
 \sigma=\frac{3/7-\alpha}{2},\qquad
 |\omega_+|^2=\frac1{7\alpha},\qquad \tau>0.
 \tag{14}
\]
In particular
\[
       \frac5{56}<\sigma<\frac4{35},\qquad
           \frac47<|\omega_+|^2<\frac57<1.
 \tag{15}
\]
The real Möbius map in (11) sends the upper half-plane into itself.
Thus \(p_+=2\omega_+/(1-\omega_+)\) has positive imaginary
part, and \(\omega_+\) is exactly the original upper endpoint
root at \(p_+\). Define
\[
             e_+=\frac{\operatorname{Log}p_+}{2\pi i},
 \qquad
             u_+=\frac{\operatorname{Log}\omega_+}{2\pi i},
 \tag{16}
\]
with both logarithms having argument in \((0,\pi)\).

## 3. Explicit containment and zero logarithmic lift

**Theorem 1.** The point (16) obeys
\[
 \frac{27}{100}<\Re e_+<\frac38,\qquad
      -\frac4{75}<\Im e_+<-\frac7{220},\qquad
       \frac16<\Re u_+<\frac14,\quad \Im u_+>0.
 \tag{17}
\]
In particular \(e_+\) is strictly inside \(E_c\). It satisfies
the original equation
\[
                         \Psi_e(e_+,1/2,-2)=0,
 \tag{18}
\]
not merely its exponentiated version.

*Proof.* Put \(s=|\omega_+|^2\). From (14),
\[
 |p_+|^2=\frac{4}{1+4\alpha+7\alpha^2},
                \qquad \frac{64}{39}<|p_+|^2<\frac{25}{13}.
 \tag{19}
\]
The elementary logarithmic bound
\(\log x\ge2(x-1)/(x+1)\) gives
\(\log(64/39)>50/103>2/5\).
Also
\[
 e^{2/3}>
  1+\frac23+\frac29+\frac4{81}=\frac{157}{81}>\frac{25}{13},
 \tag{20}
\]
so \(\log(25/13)<2/3\).
Using \(\pi<22/7\) and \(\pi>25/8\) in
\(\Im e_+=-\log|p_+|^2/(4\pi)\) proves its two height bounds.

The real and imaginary parts of \(p_+\) are proportional to
\(\sigma-s\) and \(\tau\), respectively, with the same positive
factor. Thus \(p_+\) is in the second quadrant, and
\[
          \tan(\arg p_+-\pi/2)=\frac{s-\sigma}{\tau}.
 \tag{21}
\]
Equations (15) give \(s-\sigma>16/35\), while \(\tau<1\).
On the other hand \(s-\sigma<5/8\) and
\[
 \tau^2=s-\sigma^2>\frac47-\frac{16}{1225}>\frac12
                                                    >\frac{25}{64}.
 \tag{22}
\]
Hence the ratio in (21) is between \(16/35\) and \(1\).
For \(x=\pi/25<1/7\), the elementary sine/cosine estimates give
\[
 \tan(\pi/25)<\frac{1/7}{1-1/98}=\frac{14}{97}<\frac15
                                                        <\frac{16}{35}.
 \tag{23}
\]
Therefore \(.54\pi<\arg p_+<3\pi/4\), proving the real-part
bounds on \(e_+\). Since \(\sigma>0\) and
\(\sigma/|\omega_+|<1/2\), one also has
\(\pi/3<\arg\omega_+<\pi/2\). The remaining assertions about
\(u_+\) follow from (15)--(16).

By (17), \(e_+-u_+\) has real part in \((0,1/2)\) and
negative height. The point \(e_++1/2\) has real part in
\((1/2,1)\) and negative height. The original sine arguments
therefore satisfy
\[
 0<\Im J'(e_++1/2)<\pi/2,\qquad
       -\pi/2<\Im J'(e_+-u_+)<0.
 \tag{24}
\]
It follows from (3) that
\[
 \Im\Psi_e(e_+,1/2,-2)
  =\Im J'(e_++1/2)-\Im J'(e_+-u_+)
                             +\pi(\Re u_+-1/2)
                         \in(-\pi/2,\pi).
 \tag{25}
\]
Equation (11) makes its exponential equal to one. The only
multiple of \(2\pi\) in (25) is zero, proving (18) with the
original logarithmic lift. \(\square\)

This root is nondegenerate directly from the algebra as well.
All roots of \(f\) are simple, as shown after (13), and
\[
 \frac{dp}{d\omega}=\frac{4(3\omega-1)}{(\omega+1)^3}\ne0
                                         \quad(\omega=\omega_+).
 \tag{26}
\]
The denominators in (8) do not vanish there; in particular
\(p_+-\omega_+=\omega_+(1+\omega_+)/(1-\omega_+)\ne0\).
Along the original endpoint branch,
\[
 e^{\Psi_e}-1
       =\frac{\mathfrak p_X(\omega)}
                    {(\omega+1)^2(p-\omega)} .
 \tag{27}
\]
Differentiation at (11), using (26), proves \(\Psi_{ee}\ne0\).

## 4. Strict horizontal curvature and the actual central integral

At \(a=1/2,w=-2\), the exact endpoint curvature formula in
[the complex-profile theorem, equation (4)](research_mixed_cap_early_taper_complex_profiles.md)
gives
\[
 \Psi_{ee}(e,1/2,-2)
   =-\frac{\pi}{\sin\pi e\cos\pi e}
      -\frac{2\pi}
        {\sin\pi e\sqrt{\,2-e^{-2\pi ie}\,}} .
 \tag{28}
\]
Both reciprocal denominators have positive real part for
\(e\in E_c,\ \Im e\le0\). For the first, use
\(\Re\sin(2\pi e)>0\).
For the second, the original square root has
argument in \((0,\pi/4)\), while
\(\arg\sin\pi e\in(-\pi/4,0]\).
The latter follows from
\(|\tanh(\pi\Im e)|\cot(\pi\Re e)<1\).
Their product has argument strictly between \(-\pi/4\) and
\(\pi/4\), so its reciprocal has positive real part.
Consequently
\[
                   -\Re\Psi_{ee}(e,1/2,-2)>0
                    \quad(e\in E_c,\ \Im e\le0).
 \tag{29}
\]
Compactness gives a positive uniform lower bound.

Put \(h_+=\Im e_+\) and let
\(\gamma=[.27,.49]+ih_+\), oriented from left to right.
All factorial arguments in (2) lie in their original regular
strips on a neighborhood of this contour: in particular
\(.77\le\Re(e+1/2)\le.99\).
The endpoint rectangle packet and the direct factorial expansion
therefore give the literal row symbol
\[
 \mathscr A_N(e,a,w)
   =N^{-3/2}\mathcal A(e,w)
      \sqrt{\frac{\sin\pi(e+a)}{\sin\pi a}}\,
       e^{N\Psi(e,a,w)}(1+O_{\rm hol}(N^{-1}))
 \tag{30}
\]
near \(\gamma\times\{1/2\}\times\{-2\}\).
This is the local expansion of (2), with the original
order-one factorial and \(D_N^{-1}\) phases canceled, exactly
as in the complete first-cap source. It does not use its
restricted outgoing-domain conclusion.

By (18) and (29), \(\Re\Psi\) on \(\gamma\) has its unique
maximum at \(e_+\), with a nonzero quadratic Hessian.
Its endpoints have a strict gap. The exact central integral
\[
                   I_N(a,w)=N\int_\gamma
                                      \mathscr A_N(e,a,w)\,de
 \tag{31}
\]
thus satisfies
\[
 \begin{split}
 I_N(1/2,-2)
   &=N^{-1}\mathcal B_{1/2}\,
                 e^{N\Psi(e_+,1/2,-2)}(1+O(N^{-1})),\\
 \mathcal B_{1/2}
   &=\frac{\sqrt{2\pi}\,\mathcal A(e_+,-2)\,
                   \sqrt{\cos\pi e_+}}
                         {\sqrt{-\Psi_{ee}(e_+,1/2,-2)}}\ne0 .
 \end{split}
 \tag{32}
\]
The Gaussian root has positive real part, and the sine root is
the original factorial branch. The power in (32) is
\(N\cdot N^{-3/2}\cdot N^{-1/2}=N^{-1}\); there is no
additional crossing scalar.

The implicit critical point continues to small fixed complex
neighborhoods of \(a=1/2,w=-2\). Keep the path in (31)
fixed. Moving its central portion through the continued root
introduces only short endpoint connectors within the already
strict endpoint gaps. The same local Gaussian argument gives
a holomorphic version of (32), with every fixed normalized
mixed derivative on smaller neighborhoods. The complete ordinary
boundary derivative is unchanged; the original endpoint identity
gives, for every fixed \(k\),
\[
 (-1)^k\partial_w^k I_N(1/2,w)\big|_{w=-2}
   =N^{k-1}\mathcal B_{1/2}
      \left(\frac{\tan\pi u_+}{4\pi}\right)^k
       e^{N\Psi(e_+,1/2,-2)}(1+O_k(N^{-1})).
 \tag{33}
\]
The multiplier is nonzero by (17).

## 5. Scope of the half-face anchor

Equation (31) is the retained private constant-mode integral
with its exact outside \(N\). It is only one part of the
original first-cap residue decomposition. The physical private
ends, the real cuts, the horizontal and vertical alias currents,
and the joins from the real contour to \(\gamma\) have not
been compared with (32)'s action here.

In particular the compulsory real cut values do not move when
the chosen private main height changes. Neither (29) nor (32)
shows that those cut profiles lie below a proposed universal
prefix ceiling. No bound for the whole product
\(U_{0,N}(w,-1)C_{1,N}(-1,Y)\) on the selected \(Y\)-arc
follows without those comparisons and a complete estimate of
(5). The outgoing selected halfweights, the next ordinary
supporting plane and its actual reference action remain separate.

All local source conclusions above hold at both parities; no
even-level termination was used to continue an odd-level sum.
The frozen first-cap theorems and the completed knot-family
statements are unchanged.
