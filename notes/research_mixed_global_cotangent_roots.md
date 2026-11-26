# Global conditional roots in a cotangent strip

Research proof, 4 November 2026. This is a phase and root theorem.
It does not establish dominance of the complete finite conditional sum,
an outer-period lower bound, or a mixed-word volume theorem.
Frozen manuscripts and completed source artifacts are unchanged.

## 1. Original equations

Let
\[
 {\cal P}=\{P\in\mathbb C:\Re P>0,\ |\Im P|<1/2\},\qquad
 {\cal S}=\{S\in\mathbb C:\Re S>0,\ |\Im S|<1\}.
 \tag{1}
\]
For \(P,Q\in{\cal P}\), define the inverse cotangents by
\[
 a={1\over2\pi i}\Log{P+i\over P-i},\quad
 b={1\over2\pi i}\Log{Q+i\over Q-i},\quad
 s={1\over2\pi i}\Log{S+i\over S-i}.
 \tag{2}
\]
Each ratio has positive imaginary part. The principal logarithm therefore
gives \(0<\Re a,\Re b,\Re s<1/2\), with globally holomorphic branches.

Use the original normalized primitive
\(g(z)=[\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6]/(2\pi i)\).
The conditional equations are
\[
 f_\epsilon(s;a,b)=
 g'(s+a)+g'(s+b)-(2+\epsilon)g'(s)+2\pi ia=0,
 \qquad \epsilon=0,1.
 \tag{3}
\]
Put \(A=(P-i)/(P+i)\), \(B=(Q-i)/(Q+i)\), \(U=(S-i)/(S+i)\).
Their exponentiated forms are
\((1-AU)(1-BU)=A(1-U)^{2+\epsilon}\).
Since no denominator vanishes in (1), these are equivalent to
\[
 \begin{split}
 F_0(S)&=S^2+(P+Q)S-1+i(Q-P)=0,\\
 F_1(S)&=(S+i)(S+P)(S+Q)-2i(P-i)(Q+i)=0.
 \end{split}
 \tag{4}
\]

**Theorem 1.** For each \(\epsilon=0,1\) and every
\((P,Q)\in{\cal P}^2\), (4) has exactly one root in \({\cal S}\),
counting multiplicity. The root is simple and globally holomorphic in
\((P,Q)\). Its inverse cotangent is the original zero-lift root of (3).
On compact subsets the roots stay uniformly inside the regular strips.

## 2. No boundary crossing for the quadratic

Write \(P=p+i\alpha,\ Q=q+i\beta\), where \(p,q>0\) and
\(|\alpha|,|\beta|<1/2\). On \(S=u\pm i\), \(u\ge0\),
\[
 \Im F_0(u+i)=u(2+\alpha+\beta)+2q>0,\qquad
 \Im F_0(u-i)=u(-2+\alpha+\beta)-2p<0.
 \tag{5}
\]
On \(S=iv,\ -1\le v\le1\),
\[
 \Re F_0(iv)=-1-v^2+\alpha(1-v)-\beta(1+v)<-v^2\le0.
 \tag{6}
\]
Thus no root crosses the boundary of \({\cal S}\).

At \(P=Q=1\), the roots are \(-1\pm\sqrt2\); exactly one belongs
to \({\cal S}\). Along any compact parameter homotopy inside
\({\cal P}^2\), the polynomial is monic with bounded coefficients, so
its roots cannot escape to infinity. The argument principle on a
sufficiently large finite rectangle now proves the quadratic assertion.

## 3. No boundary crossing for the cubic

On \(S=iv,\ -1\le v\le1\), direct expansion gives
\[
 \Im F_1(iv)=(v-1)pq+
 2(\alpha-1)(\beta+1)-(v+1)(\alpha+v)(\beta+v).                 \tag{7}
\]
The last two terms are bilinear in \(\alpha,\beta\). At the four
corners \((\alpha,\beta)=(\pm1/2,\pm1/2)\), they are respectively
\[
 -\tfrac32-(v+1)(v+\tfrac12)^2,\quad
 -\tfrac32-(v+1)(v-\tfrac12)^2,\quad
 -\tfrac12+(v+1)(\tfrac14-v^2),\quad
 -\tfrac92+(v+1)(\tfrac14-v^2).
\]
If \(|v|\ge1/2\), the latter product is nonpositive. Otherwise it
is at most \((3/2)(1/4)=3/8\). Therefore (7) is at most \(-1/8\).
This excludes the entire left boundary, including its two corners.

On the upper boundary \(S=u+i,\ u>0\), solve \(F_1=0\) for \(P\).
Its denominator is \(u(u+Q+3i)\), which is nonzero. The resulting
imaginary part is
\[
 \Im P=-1-
 {2\{4q+uq(u+q)+u(\beta+1)^2\}
  \over u\{(u+q)^2+(\beta+3)^2\}}<-1.
 \tag{8}
\]
This contradicts \(P\in{\cal P}\).

On the lower boundary \(S=u-i,\ u>0\), the equation would read
\[
 {P+u-i\over P-i}\,{Q+u-i\over Q+i}={2i\over u}.               \tag{9}
\]
The first factor equals \(1+u/(P-i)\), with real part greater than
one and positive imaginary part. Its argument lies in \((0,\pi/2)\).
The numerator of the second factor has positive real and negative
imaginary parts, while its denominator has positive real and positive
imaginary parts. Its argument lies in \((-\pi,0)\).
The product has an argument in \((-\pi,\pi/2)\), which cannot equal
the argument of \(2i/u\), even modulo \(2\pi\). This excludes the
lower boundary.

For a purely exact base count take \(P=Q=1\), so
\[
 F_1(S)=S^3+(2+i)S^2+(1+2i)S-3i.
\]
Use radius \(r=1/20\) and the three rational centers
\[
 c_1=3/5+i/3,\quad c_2=-21/10+11i/20,\quad
 c_3=-1/2-19i/10.
\]
Writing \(F_1(c+w)=F_1(c)+F_1'(c)w+(3c+2+i)w^2+w^3\),
the rational lower bounds for
\[
 r\max(|\Re F_1'(c)|,|\Im F_1'(c)|)
 -|\Re F_1(c)|-|\Im F_1(c)|
 -r^2(|\Re(3c+2+i)|+|\Im(3c+2+i)|)-r^3
\]
are exactly \(5621/43200,\ 1971/8000,\ 2359/8000\).
They are positive. Rouché's theorem gives one root in each disk.
The disks are disjoint, the first lies inside \({\cal S}\), and the
other two lie strictly in the left half-plane. Degree three exhausts
all roots. No numerical root count is used.

The same monic-polynomial homotopy argument as in Section 2 now proves
the cubic root count everywhere. A count of one with multiplicity
implies simplicity. Local implicit roots agree by uniqueness, proving
global holomorphy.

## 4. The original logarithmic lift and local coercivity

All arguments \(s,a,b,s+a,s+b\) remain in their original strips.
The function \(f_\epsilon\) in (3) is holomorphic on the connected
parameter domain and has exponential identically one, hence is a
constant multiple of \(2\pi i\).

For \(\epsilon=0,\ P=Q=1\), the root is \(s=3/8\), \(a=b=1/4\),
and the original sine-log formula gives \(f_0=0\) exactly.
For \(\epsilon=1\), use the first Rouché disk above and
\(U=(S-i)/(S+i)\). The outward checker verifies on its containing
rectangle
\[
 \left|\Im\{2\Log(1+iU)-3\Log(1-U)+i\pi/2\}\right|<\pi.
 \tag{10}
\]
At the actual polynomial root the exponential is one, so this expression
is zero. It is exactly (3) at \(a=b=1/4\). Thus the constant lift
is zero for both types throughout \({\cal P}^2\).

The [triangle-form determinant](research_mixed_plateau_accretivity.md)
applies at every resulting root: both outer cotangents have imaginary
parts below \(1/2\), and the inner one below one, all with positive real
parts. It follows that \(-\Re Q_{ss}>0\), and the corresponding
allocated unsummed and Schur quadratic forms are positive.
These inequalities are uniform on compact subsets. They give
nondegeneracy and local horizontal coercivity. The cotangent-domain
preimage need not be convex in the angle variables, so no global
horizontal maximum is inferred merely from this statement.

The half-width hypothesis cannot simply be replaced by one. For
\(P=1+99i/100,\ Q=1-99i/100\), the quadratic becomes
\(S^2+2S+49/50\), with both roots negative real.

## 5. Both quadratic outer tapers lie in this domain

Let \(l=11/50\), \(H=57/1000\), and suppose
\[
 0<x<1/2,\qquad
 |h(x)|\le H\min\{1,(x/l)^2\}.                               \tag{11}
\]
This includes both previously used quadratic taper profiles, all
actual typed heights, and the selected positive height \(7/500\).
The real part of \(\cot\pi(x+ih)\) is positive, and
\[
 |\Im\cot\pi(x+ih)|
 ={\sinh(2\pi|h|)\over\cosh(2\pi h)-\cos(2\pi x)}
 \le {\sinh(2\pi H)\over2\sin^2(\pi l)}<\tfrac12.             \tag{12}
\]
For \(x\le l\), use convexity of sinh and concavity of sine:
the numerator is at most \((x/l)^2\sinh(2\pi H)\), while the
denominator is at least \(2(x/l)^2\sin^2(\pi l)\).
For \(x\ge l\), use \(|h|\le H\) and
\(\sin\pi x\ge\sin\pi l\). The last inequality in (12) is a single
outward scalar comparison.

Consequently every pair of outer angles on either taper, away from its
zero endpoint and the half-period endpoint, has a globally specified
original conditional critical root of either type. Compact subarcs
have uniform root and local coercivity bounds. The inner height may
grow without bound as an outer angle approaches zero; Theorem 1 does
not impose an artificial fixed height rectangle.

The remaining source obligations are literal: a contributing deformation
of the complete finite sum, its endpoint and revived-row comparisons,
all aliases, and a nonzero full-period coefficient. None follows from
root existence or local coercivity alone.

Reproduction:

    python3 experiments/check_mixed_global_cotangent_roots.py --precision 256

The checker uses exact polynomial identities and rational Rouché
inequalities, plus the outward base-lift and taper bounds. It neither
samples words nor substitutes a numerical root count.
