# Complete boundary coefficients throughout the interior index interval

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The complete-boundary asymptotic was previously proved for index ratios
below \(1/2\). The same nonzero contribution in fact persists throughout
the open interval \((0,1)\). Above \(1/2\), the real part of the phase is
not concave on every horizontal segment. We replace that unnecessary
condition by an exact proof that each horizontal segment has only one
maximum. The rows beyond the midpoint have a separate strict bound.

This extension is useful for the first factor of an open mixed word:
its original summation can involve indices greater than \(N/2\).
It is still a statement about a boundary coefficient, not the asymptotic
of the fully contracted word.

## 1. The original coefficient and the claim

Use the notation of
[the complete-boundary coefficient theorem](research_complete_boundary_coefficient_asymptotic.md).
In particular,
\[
 \begin{split}
 S_l&=\prod_{h=1}^l2\sin(\pi h/N),\qquad q=e^{\pi i/N},\\
 E_{l,k}&=(-1)^k e_l^{(k)}(-2),\\
 C_{j,N}^{(k)}&=\sum_{l=0}^j
           \frac{q^{jl}E_{l,k}}{S_lS_{j-l}},\\
 b_{j,N}^{(k)}(-2)&=(-1)^k\delta_j^{-1}C_{j,N}^{(k)},\qquad
 \delta_j=\exp\left(\frac{\pi i}{2N}((N-1)j-j^2)\right).
 \end{split}
 \tag{1}
\]
The polynomials \(e_l\) are the original Newton polynomials. Thus these
are ordinary boundary derivatives of the actual coefficient, including
the endpoint zero at odd levels and its nonzero derivatives.

On \(0<\Re z<1\), let \(J'(z)=\Log(2\sin\pi z)\), with the branch
continued from positive real sine. Set
\[
 \begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 u_c(e)&=\frac1\pi\arctan\frac{i+\sqrt{1-2e^{2\pi ie}}}{2},\\
 A_k(e)&=\frac{\sqrt{2\pi}}{\sqrt{-F_{uu}(e,u_c(e))}}
 \frac{(\tan(\pi u_c(e))/(4\pi))^k}
 {(2\sin\pi u_c(e))^{3/2}
                 (2\sin\pi(e-u_c(e)))^{1/2}}.
 \end{split}
 \tag{2}
\]
All branches agree with the earlier theorem for \(0<e<1/2\);
they are continued along the real interval. The Gaussian square root
has positive real part.

**Theorem 1.** For every compact interval \(I\subset(0,1)\) and every
fixed integer \(k\ge0\),
\[
 C_{j,N}^{(k)}
   =N^{k-3/2}A_k(j/N)
        \exp\{NF(j/N,u_c(j/N))\}\{1+O_{I,k}(N^{-1})\},
       \qquad j/N\in I.
 \tag{3}
\]
The coefficient \(A_k\) is nonzero. The statement holds uniformly
over the physical integers \(j\), at both level parities.

The same formula holds on a fixed complex neighborhood of \(I\) for
the specified finite continuation
\[
 C_{N,k}(e)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}E_{l,k}}{S_lG_N(Ne-l)}.
 \tag{4}
\]
Its normalized relative error and every fixed \(e\)-derivative are
uniform on smaller neighborhoods. Here \(G_N\) is the exact sine
factorial, not an arbitrary interpolation of the physical values.
Formula (4) is the same finite function as in
[the complex-index theorem](research_complete_boundary_complex_index.md).

The earlier proofs cover compact subsets below \(1/2\).
We prove the additional assertions on \([1/2,1)\), with strict margins
that also hold across the midpoint.

## 2. The continued critical point

Write
\[
 \sqrt{1-2e^{2\pi ie}}=a+ib,\qquad 1/2<e<1.
 \tag{5}
\]
The principal square root has \(a>0\) and \(0<b<1\).
Indeed its imaginary part is positive, and if \(R=a^2+b^2\), then
the unit-modulus equation for \(e^{2\pi ie}\) gives
\[
 (R-1)^2+4b^2=4,\qquad
 R=1+2\sqrt{1-b^2}.
 \tag{6}
\]
Here \(1<R<3\). The bound \(b<1\) is strict in the open interval;
the endpoint \(b=1\) occurs only as \(e\to1\).

Put \(t=(a+i(1+b))/2\). The identity
\[
 \arctan t=\frac1{2i}
       \Log\frac{1+it}{1-it}
 \tag{7}
\]
uses its continuous branch. Both \(1+it=(1-b+ia)/2\) and
\(1-it=(3+b-ia)/2\) have positive real part. Their quotient has
argument in \((0,\pi)\) and modulus less than one.
Moreover its real part has the sign of
\[
 3-2b-R=2(1-b-\sqrt{1-b^2})<0.
 \tag{8}
\]
Consequently
\[
             \frac14<\Re u_c(e)<\frac12,\qquad
                      H(e):=\Im u_c(e)>0.
 \tag{9}
\]
Also \(0<\Re(e-u_c)<1\). None of the sine or cosine factors in
the critical equation crosses a divisor. The algebraic equation
used in the earlier proof continues identically, and its logarithmic
lift is continuous and integer valued after division by \(2\pi i\).
It is zero at \(e=1/2\). Hence \(F_u(e,u_c)=0\) with the original
lift throughout \(1/2<e<1\).

At the midpoint, \(u_c=1/4+i\log(3)/(4\pi)\). This agrees with
the limit from either side and lies strictly inside the regular
phase domain. On every compact subinterval the point stays away
from all its divisors.

## 3. One horizontal maximum, without a false concavity assertion

Fix \(1/2<e<1\) and a height \(H>0\). For \(u=x+iH\),
\(0<x<1/2\), the logarithmic derivative is
\[
 F_u=2\Log\cos\pi u+\Log\sin\pi(e-u)
                 -3\Log\sin\pi u+i\pi e.
 \tag{10}
\]
Put
\[
 C=\cosh(2\pi H)>1,\quad
 c=\cos(2\pi x),\quad s=\sin(2\pi x)>0,\quad
 C_e=\cos(2\pi e),\quad S_e=\sin(2\pi e)<0.
 \tag{11}
\]
The square of the positive ratio whose logarithm is \(\Re F_u\)
is
\[
 \mathcal Q(x)=
  \frac{(C+c)^2(C-C_ec-S_es)}{(C-c)^3}.
 \tag{12}
\]
All factors in this quotient are positive. The numerator of
\(\mathcal Q-1\) is
\[
 \begin{split}
 D&=c\,A-S_es(C+c)^2,\\
 A&=(1-C_e)(C+c)^2+4C(C-c)>0.
 \end{split}
 \tag{13}
\]
For \(0<x\le1/4\), one has \(c\ge0\), so \(D>0\).
For \(1/4<x<1/2\), put \(v=-c/s=-\cot(2\pi x)>0\).
Then \(D=0\) is exactly
\[
 v\left(1-C_e+\frac{4C(C-c)}{(C+c)^2}\right)=-S_e.
 \tag{14}
\]
The left side increases strictly from zero to infinity:
\(v\) increases strictly, \(c\) decreases, and
\[
 \frac{d}{dc}\frac{C-c}{(C+c)^2}
                    =-\frac{3C-c}{(C+c)^3}<0.
 \tag{15}
\]
It follows that \(\Re F_u\) is positive before exactly one point
and negative after it. At that point its derivative is strictly
negative, since the left side of (14) has strictly positive
derivative and all factors removed in reaching (14) are positive.

Thus \(\Re F(e,x+iH)\) has exactly one maximum on the entire
horizontal interval, and that maximum is nondegenerate.
Taking \(H=H(e)\), the point in (9) is that maximum. In particular
\[
                     \Re[-F_{uu}(e,u_c)]>0.
 \tag{16}
\]
At \(e=1/2\), \(S_e=0\), and (13) has precisely the sign of \(c\);
the same assertions hold with \(x=1/4\).
These arguments do not claim that the second derivative has one sign
away from the maximum. In fact such global concavity can fail here.

## 4. Both limiting vertical sides

The actual deformation will stay inside the phase domain. We first
compare its limiting sides. At \(u=iy\), \(y>0\), the first cosine
has argument zero, \(\arg\sin\pi u=\pi/2\), and
\(\arg\sin\pi(e-iy)\in(-\pi/2,\pi/2)\). Equation (10) gives
\[
                       \Im F_u(e,iy)<-\pi(1-e)<0.
 \tag{17}
\]
At \(u=1/2+iy\), with \(e>1/2\), the cosine has argument
\(-\pi/2\), \(\sin\pi u\) is positive, and
\(\arg\sin\pi(e-1/2-iy)\in(-\pi/2,0)\). Hence
\[
                  \Im F_u(e,1/2+iy)<-\pi(1-e)<0.
 \tag{18}
\]
At \(e=1/2\), the last sine has argument \(-\pi/2\), and the
same strict inequality follows directly.
Since \(\partial_y\Re F=-\Im F_u\), the real phase increases
strictly up both sides, from their finite real endpoint limits
to height \(H(e)\).

Section 3 puts both upper endpoints strictly below
\(\lambda(e)=\Re F(e,u_c(e))\). Thus both entire vertical
segments, including their real endpoints, have a strict gap.
Compactness gives uniform gaps on every compact \(e\)-interval
in \([1/2,1)\). Choose interior cuts sufficiently close to
zero and \(1/2\); their vertical segments and the omitted real
strips retain a fixed positive part of those gaps.

## 5. The physical rows above the midpoint

For real \(0\le u\le1\), write
\[
 \mathcal V(u)=2\int_0^u\log(2|\cos\pi t|)\,dt-2J(u).
 \tag{19}
\]
The uniform finite-product bounds in the earlier proof give
\(E_{l,k}\le N^{C_k}e^{N\mathcal V(l/N)}\), including the
odd zero and its derivatives. When \(u\le1/2\),
\(\mathcal V(u)=V_0(u)=-2J(1/2-u)-2J(u)\), whereas
\(\mathcal V(1-u)=-\mathcal V(u)\).

For \(1/2\le u\le e\), the real summand entropy is
\(\mathcal V(u)-J(u)-J(e-u)\). Put
\(x=u-1/2\) and \(a=e-1/2\), so \(0\le x\le a<1/2\).
Its excess over the endpoint value at \(u=1/2\) is exactly
\[
 \begin{split}
 &\mathcal V(u)-J(u)-J(e-u)+J(a)\\
 &\qquad=-V_0(x)+J(1/2-x)+J(a)-J(a-x)\le0.
 \end{split}
 \tag{20}
\]
Indeed \(V_0(x)\ge0\). Also \(J'\) is increasing on \((0,1/2)\),
so
\[
 J(a)-J(a-x)
     =\int_{a-x}^a J'(t)\,dt
     \le\int_{1/2-x}^{1/2}J'(t)\,dt=-J(1/2-x).
 \tag{21}
\]
At \(x=0\) use continuity. Therefore all these rows have rate
at most \(-J(e-1/2)\), the real phase at the limiting upper
endpoint of Section 4. They lie strictly below \(\lambda(e)\).
This proves a uniform bound for the entire extra physical interval,
not just for its two endpoints.

## 6. The actual sum and its complex continuation

On the retained interval, the exact factorial summand and its symbol
are exactly those of the earlier coefficient theorem. Choose half-grid
cuts near the two interior cuts of Section 4 and use the rectangle
with horizontal heights \(\pm H(e)\). The kernel
\((1-e^{-2\pi iNu})^{-1}\) has the original residues.
Its constant mode deforms to the selected upper horizontal line,
retaining both upper vertical currents.

The reflection identity is unchanged:
\[
 \Re F(e,x-iy)=\Re F(e,x+iy)+2\pi ey.
 \tag{22}
\]
Consequently the two horizontal aliases lose respectively
\(2\pi(1-e)H(e)\) and \(2\pi H(e)\). Both losses are strictly
positive on compact subintervals of \((0,1)\).
The half-grid vertical kernel bounds, (17)--(18), and the same
reflection identity control both lower vertical currents as well.
Every original physical row outside the retained interval is covered
by Section 4 or Section 5. The unique nondegenerate horizontal
maximum gives the coefficient (2), with power
\(N^{k-2}\cdot N\cdot N^{-1/2}=N^{k-3/2}\).
The first cubic Gaussian correction is odd, giving the relative
error \(O(N^{-1})\). This proves (3).

For the canonical sum (4), it remains to control rows that vanish
on the physical grid and revive at a complex index. At a real
\(e\ge1/2\) their upper rate is
\[
 H_{\mathrm{ext}}(e,u)=\mathcal V(u)-J(u)+J(u-e),
                         \qquad e\le u\le1.
 \tag{23}
\]
Every term on the right is nonpositive: \(u\ge1/2\) gives
\(\mathcal V(u)\le0\) and \(J(u)\ge0\), while
\(0\le u-e\le1-e\le1/2\) gives \(J(u-e)\le0\).
In contrast, Section 4 gives
\[
                 \lambda(e)>-J(e-1/2)\ge0.
 \tag{24}
\]
This leaves a uniform positive gap on every compact interval in
\([1/2,1)\).

The regularized finite-product estimate for (4) bounds the cost of
a complex displacement of size \(\delta\) by
\(C\delta(1+|\log\delta|)\) in the exponential rate, uniformly
through the physical zeros. It was proved for this same reciprocal
factorial sum in the complex-index theorem; its proof applies on
every compact subinterval of \(0<e<1\). Equations (20) and (23)
supply the additional real-row comparisons needed here.

Fix a real reference and its contour with strict gaps. The middle
factorial symbol and every contour-current bound persist on a small
complex neighborhood. The simple critical point continues
holomorphically by (16). The Gaussian argument therefore gives
(3) for the fixed finite function (4) on that neighborhood.
Finitely many such neighborhoods cover \(I\), including \(e=1/2\).
They use the same finite function, and the critical branch agrees
by continuation from (2). The normalized relative errors are
holomorphic, so Cauchy's estimates give all fixed derivatives on
smaller neighborhoods. This proves Theorem 1.

The theorem does not specify how large those complex neighborhoods
are. In particular it cannot yet be used at an arbitrary remote
critical point of the first-vertex polynomial in an open word.

## 7. The whole boundary polynomial near the complete color

The preceding theorem need not be used only as a list of derivatives.
There is a joint asymptotic for the actual boundary polynomial. Define
\[
 \mathcal C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)}.
 \tag{25}
\]
At a physical index this is the original boundary coefficient
multiplied by \(\delta_j\). In particular
\(\partial_w^k\mathcal C_N(e,-2)=(-1)^kC_{N,k}(e)\).
For a small complex \(t\), write \(w=-2\cos t\), and set
\[
 \begin{split}
 \mathcal F(e,u,t)={}&
   -J(1/2-u+t/(2\pi))-J(1/2-u-t/(2\pi))\\
 &-3J(u)-J(e-u)+i\pi eu.
 \end{split}
 \tag{26}
\]
Its critical point \(\mathfrak u(e,t)\) continues \(u_c(e)\).
Let \(\mathcal S(e,w)=\mathcal F(e,\mathfrak u(e,t),t)\) and
\[
 \mathcal A(e,w)=
 \frac{\sqrt{2\pi}}
      {\sqrt{-\mathcal F_{uu}(e,\mathfrak u(e,t),t)}}
 \frac1{(2\sin\pi\mathfrak u(e,t))^{3/2}
         (2\sin\pi(e-\mathfrak u(e,t)))^{1/2}}.
 \tag{27}
\]

**Theorem 2.** For every compact \(I\subset(0,1)\), these functions
are holomorphic on a fixed complex neighborhood of
\(I\times\{-2\}\), and \(\mathcal A\ne0\). On a possibly smaller
such neighborhood,
\[
 \mathcal C_N(e,w)
   =N^{-3/2}\mathcal A(e,w)e^{N\mathcal S(e,w)}
                              \{1+O(N^{-1})\}.
 \tag{28}
\]
The normalized relative error is holomorphic, uniformly with every
fixed joint derivative on smaller neighborhoods. Both level parities
and the entire original boundary polynomial are retained.

*Proof.* The exact interpolation for \(e_l(-2\cos t)\), equation (8)
of the original coefficient proof, is a quotient of four prescribed
sine factorials. On the middle contour it has the uniform symbol
given there, holomorphic for small complex \(t\). Its two midpoint
factorials each have symbol
\(G_N(Nx-1/2)=\sqrt N\,e^{NJ(x)}(1+O(N^{-1}))\).
Thus the exact central summand has phase (26), power \(N^{-2}\),
and amplitude
\((2\sin\pi u)^{-3/2}(2\sin\pi(e-u))^{-1/2}\).
There is no missing order-one factor depending on \(t\).

We must also control the whole finite sum when \(w\ne-2\).
The literal Newton product gives, for \(|w+2|\le\delta\),
\[
 |e_l(w)|\le S_l^{-2}
       \prod_{h=0}^{l-1}
       \bigl(4\cos^2(\pi(h+1/2)/N)+\delta\bigr).
 \tag{29}
\]
For fixed \(\delta>0\), the regularized logarithm in this product
has bounded variation, so its Riemann-sum error is \(O_\delta(1)\),
uniformly in the upper index. Its integral exceeds the unregularized
one by at most \(C\sqrt\delta\), uniformly for \(0\le l/N\le1\).
For a direct bound, near \(x=1/2\) use
\(|\cos\pi x|\ge2|x-1/2|\) and extend
\(\int\log(1+\delta/(16(x-1/2)^2))\,dx\) to the real line.
Its exact integral is \((\pi/2)\sqrt\delta\);
away from that point the same bound is immediate.
Consequently
\[
 |e_l(w)|\le C_\delta N^C
          \exp N\{\mathcal V(l/N)+C\sqrt\delta\}.
 \tag{30}
\]
This argument includes the odd exact zero and never divides by it.

Combine (30) with the reciprocal-factorial bounds used for (23).
A small complex displacement of \(e\) has the already controlled
cost \(C\delta_e(1+|\log\delta_e|)\). The strict real-row gaps from
Sections 4--6 therefore persist for small fixed \(\delta,\delta_e\).
On the retained contour all factors are regular, so its side and
alias gaps persist by continuity. The nondegenerate critical point
continues by the implicit function theorem, and the same complete
contour calculation yields (28).

Both (26) and the exact interpolation are even in \(t\).
Uniqueness makes \(\mathfrak u\), its action and its coefficient
even as well. They are holomorphic in \(t^2\), and
\(w+2=t^2+O(t^4)\), so they descend holomorphically to the ordinary
color \(w\). This establishes a neighborhood in the actual color,
not only in a square-root parameter. Compactness and Cauchy's
formula give the stated uniform joint derivative estimates.
\(\square\)

At \(w=-2\), \(\mathcal S_w=-\tan(\pi u_c)/(4\pi)\), so the leading
ordinary derivatives of (28) recover (2)--(3). The proof of the whole
function did not infer a uniform neighborhood merely from those
derivatives. The size of the complex neighborhood remains unspecified;
no first-vertex or complete mixed-word asymptotic is asserted.

## 8. Reproduction

The focused checker verifies the horizontal ratio identity, its
monotonicity reduction, the phase reflection, and the powers and
branch relations used above. It also evaluates the original finite
boundary sums at indices on both sides of \(N/2\), including both
parities and derivative orders zero, one and two. Those finite
comparisons check the normalization; the theorem over all interior
indices follows from the analytic argument.

The same script evaluates the whole original polynomial at two small
complex displacements from \(w=-2\), on both sides of \(e=1/2\)
and at both level parities. These 36 comparisons check the
color-dependent action and leading amplitude in Theorem 2 against
the literal finite Newton products. The additional 120 complete-color
comparisons check derivative orders zero, one and two.
They are diagnostics for the formulas, not a proof of a uniform
asymptotic neighborhood.

Run
\(\texttt{python3 experiments/check_complete_boundary_full_index_interval.py}\).
