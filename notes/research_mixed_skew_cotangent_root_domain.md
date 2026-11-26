# Conditional roots on a cotangent strip adapted to the first cap

Research deduction, 7 November 2026. The symmetric bound
\(|\Im\cot\pi z|<1/2\) used in the earlier conditional-root
theorem is unnecessarily restrictive for a first cap with a negative
outgoing height. This note proves a different product domain for the
same original quadratic and cubic equations. It contains the entire
early first-cap taper, including the wider negative heights of type
four. It does not yet prove that every adjoining ordinary coordinate
belongs to this domain, or extend any finite-source estimate.

## 1. A nonsymmetric interval for the imaginary cotangent

Put
\[
 l=-1/6,\qquad u=37/50,\qquad
 \mathcal P_*={P:\Re P>0,\ l\le\Im P\le u\},
 \qquad \mathcal S={S:\Re S>0,\ |\Im S|<1\}.
 \tag{1}
\]
Use the original equations and branches of
[the global cotangent theorem](research_mixed_global_cotangent_roots.md):
\[
 \begin{split}
 F_0(S)&=S^2+(P+Q)S-1+i(Q-P),\\
 F_1(S)&=(S+i)(S+P)(S+Q)-2i(P-i)(Q+i),\\
 a&=\frac1{2\pi i}\Log\frac{P+i}{P-i},\quad
 b=\frac1{2\pi i}\Log\frac{Q+i}{Q-i},\quad
 s=\frac1{2\pi i}\Log\frac{S+i}{S-i}.
 \end{split}
 \tag{2}
\]
All three inverse-cotangent ratios have positive imaginary part when
their arguments have positive real part. Thus these are the original
holomorphic choices with real parts between zero and one half.

**Theorem 1.** For every \((P,Q)\in\mathcal P_*^2\), each
polynomial in (2) has exactly one root in \(\mathcal S\),
counting multiplicity. The root is simple and depends holomorphically
on the inputs, including on a neighborhood of every compact subset
of the closed-height domain (1). Its inverse cotangent solves the
original conditional equation with zero logarithmic lift.

*Quadratic boundary check.* Write \(P=p+i\alpha\),
\(Q=q+i\beta\), with \(p,q>0\). On the horizontal sides
\(S=v\pm i\), \(v\ge0\), the old identities give
\[
 \Im F_0(v+i)=v(2+\alpha+\beta)+2q>0,
 \qquad
 \Im F_0(v-i)=v(-2+\alpha+\beta)-2p<0.
\]
Indeed \(2+2l>0\) and \(-2+2u<0\). On the left side,
\(-1\le v\le1\),
\[
 \begin{split}
 \Re F_0(iv)
 &=-1-v^2+\alpha(1-v)-\beta(1+v)\\
 &\le-1+u-l-(u+l)v-v^2
 \le-\frac{251}{22500}<0.
 \end{split}
 \tag{3}
\]
The last inequality completes the square, using
\(u-l=68/75\) and \(u+l=43/75\).

*Cubic boundary check.* The same left-side expansion as in the
original proof is
\[
 \Im F_1(iv)=(v-1)pq+\mathcal E(\alpha,\beta,v),
 \quad
 \mathcal E=2(\alpha-1)(\beta+1)
                      -(v+1)(\alpha+v)(\beta+v).
 \tag{4}
\]
For fixed \(v\), the last expression is bilinear in
\((\alpha,\beta)\), so its maximum on the rectangle is
attained at a corner. If \(\alpha=\beta=l\) or
\(\alpha=\beta=u\), its last product is nonnegative and
its constant is respectively \(-35/18\) or \(-1131/1250\).
For either mixed corner the product can be negative only on
\(-u<v<-l\). There
\[
 -(v+\alpha)(v+\beta)\le (u-l)^2/4,
 \qquad 0\le v+1\le7/6.
\]
The larger mixed-corner constant occurs at
\((\alpha,\beta)=(u,l)\) and is \(-13/30\).
Consequently all four corners satisfy
\[
 \mathcal E\le-\frac{13}{30}
       +\frac76\frac{(68/75)^2}{4}
       =-\frac{6533}{33750}<0.
 \tag{5}
\]
The omitted term \((v-1)pq\) is nonpositive.

On the upper side \(S=v+i\), \(v>0\), solving for
\(P\) gives exactly the expression in equation (8) of the
original theorem, whose imaginary part is less than \(-1\).
This contradicts \(\alpha\ge-1/6\). On the lower side,
the factorization in its equation (9) still applies: \(\alpha<1\)
makes the first factor have argument in \((0,\pi/2)\), and
\(-1<\beta<1\) makes the second have argument in \((-\pi,0)\).
Their product cannot be \(2i/v\). Thus no cubic root lies on
the boundary of \(\mathcal S\).

*Root count and lift.* At \(P=Q=1\), the original proof counts
exactly one root of each polynomial in \(\mathcal S\), with
its original zero logarithmic lift. Its quadratic count is explicit;
its cubic count uses the three displayed rational Rouché disks.
Join any new parameter pair to this base pair by a straight segment
in (1). The boundary exclusions (3)--(5) and the horizontal-side
checks apply throughout. The polynomials are monic with bounded
coefficients on this compact parameter segment, so roots cannot
escape to infinity. Their inside count remains one. In particular
the selected root is simple, and local implicit branches glue by
uniqueness. The strict exclusions also supply neighborhoods at the
closed height faces of (1).

The original unexponentiated conditional residual is holomorphic
and its exponential is one. Connectedness and its zero base value
therefore give zero lift on the whole new domain. No new root
evaluation or logarithm normalization is introduced. \(\square\)

The usual local coercivity also survives. If the inner and outer
cotangents are \(S=v+iw\), \(P=p+i\alpha\), then
\(v,p>0\), \(|w|<1\), and \(|\alpha|<1\). Hence
\[
 |pw-v\alpha|<p+v.
\]
The exact triangle-form determinant is positive. Both diagonal
entries are positive as well, so the real negative Hessian of each
pair is positive definite. The original own factorials and allocated
halfweights add nonnegative real diagonal terms, and the chirp has
zero real Hessian. The full and eliminated conditional Hessians are
therefore accretive on this domain, uniformly on compact subsets.
As before, this is local coercivity, not a whole-sum dominance claim.

## 2. The early first-cap taper belongs to the new strip

Let
\[
 .1\le x\le.22,\quad d=x-.1,\quad
 -.9d\le h\le\frac7{40}d,
 \qquad z=x+ih.
 \tag{6}
\]
These bounds include the original first-cap heights multiplied by
the affine cutoff \((x-.1)/.12\). Additional fixed multipliers
between zero and one preserve the inequalities. Since
\(0<x<1/2\), \(\Re\cot\pi z>0\).

For positive height, the original minimum-neighbor trigonometric
estimate gives
\[
 |\Im\cot\pi z|
 \le\frac{121\sinh(.042\pi)}
           {240\sin^2(.22\pi)}<\frac16.
 \tag{7}
\]
Here is the same argument with its constants retained. The identity
\(\rho(x)\le(125/6)x^2\), for
\(\rho=(x-.1)/.12\), and monotonicity of \(\sin t/t\)
give \(\rho/\sin^2\pi x\le121/[120\sin^2(.22\pi)]\).
Convexity gives \(\sinh(.042\pi\rho)\le\rho\sinh(.042\pi)\),
while the cotangent denominator is at least \(2\sin^2\pi x\).
Finally \(\sin(.22\pi)>127/200\) follows from the sine
lower polynomial at \(.69\), and \(\sinh(.042\pi)<133/1000\)
follows from \(.042\pi<33/250\) and
\(\sinh t\le t/(1-t^2/6)\). Substitution proves (7):
\(6\cdot121\cdot.133=96.558<96.774=240(.635)^2\).
The imaginary cotangent is negative in this case.

For negative height put \(t=2\pi|h|\), \(K=40/7\).
Then \(0\le t\le(9\pi/5)d\le Kd\). The following
three pairs of constants satisfy \(\sin\pi x>kx\)
and \(\sinh t\le St\) on their stated intervals:
\[
 \begin{array}{c|c|c}
 x\text{ interval}&k&S\\\hline
 [.1,.19]&59/20&21/20\\
 [.19,.205]&73/25&16/15\\
 [.205,.22]&127/44&13/12
 \end{array}
 \tag{8}
\]
For the first two sine constants, use
\(\sin\pi x/x\ge157/50-(22/7)^3x^2/6\) at the upper
endpoint. For the last use (7) and decreasing \(\sin t/t\).
For the sinh constants use \(t/(1-t^2/6)\) with respective
upper bounds \(18/35\), \(3/5\), and \(594/875\).
The last satisfies \((594/875)^2<6/13\).

The exact cotangent formula and \(\cosh t\ge1+t^2/2\)
now give
\[
 0\le\Im\cot\pi z
 \le\frac{St}{2k^2x^2+t^2/2}
 \le\frac{SKd}{2k^2(d+.1)^2+K^2d^2/2}.
 \tag{9}
\]
The final rational function of \(t\) is increasing up to
\(Kd\), since \(Kd<2kx\). For example
\(d/x\le6/11\), and \(K(6/11)<5<2k\).
To make (9) smaller than \(37/50\), clear its positive
denominator. For the three rows in (8), the resulting quadratic
\[
 \frac{37}{50}\{2k^2(d+.1)^2+K^2d^2/2\}-SKd
\]
is respectively greater than
\[
 24.9d^2-3.43d+.128,\qquad
 24.7d^2-3.572d+.126,\qquad
 24.4d^2-3.725d+.123.
 \tag{10}
\]
Each coefficient comparison is rational. The first quadratic has
negative discriminant and positive leading coefficient. The second
increases for \(d\ge.09\), and its value at \(.09\) is
\(.00459\). The third increases for \(d\ge.105\), and
its value there is \(.000885\). Thus all are positive on the
prescribed intervals. This proves
\[
             -1/6<\Im\cot\pi z<37/50
\]
throughout (6), including its real boundary.

Theorem 1 can therefore be used for a conditional block when both
its outer coordinates are in this cotangent domain. This includes
two coordinates satisfying (6). It does not assert that every actual
ordinary neighbor of a first cap satisfies (6), or (1): some full
typed ordinary enclosures permit larger positive heights. Their
correlation or a further domain argument must still be retained.
No ordinary transport sign or finite-source estimate is inferred
from the new root domain alone.
