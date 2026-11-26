# Factorial deficiency of the actual ordinary symbol logarithm

Private written proof, 18 November 2026.

The ordinary normal-symbol logarithm of the literal finite word has a
factorial bound in its deficiency, rather than in its full quantum
order. The estimate is uniform on fixed small meridian, field and
independent-mark disks. It also survives the regular hard Wick
contractions. No operator logarithm is summed, and no infinite Ward
operator is applied to an analytic source.

## 1. Statement and the two gradings

Use the actual signed crossings, original pivots and zero framing of
[F], on a meridian disk about \(\alpha\ne0,1\). Retain the same finite
word and highest cut as [H] and [P]. Move only the unmarked invertible
classical substitutions to the right. Write its relative operator as
\(A_h\), and its ordinary normal symbol as \(S_h(Z,P,\mathbf t)\).
Here \(e^{t_i}\) are independent stage marks; \(t_i=hm_i\) is the
original clock specialization. All fixed linear specializations to
matching-lattice clocks are retained.

Scale the fields by \(h^{-1/2}\), and take the commutative logarithm:
\[
 \log S_h(h^{-1/2}Z,h^{-1/2}P,\mathbf t)
       =\sum_{a\ge0}h^{a-1}\mathcal P_a(Y,Z,P,\mathbf t).
 \tag{1}
\]
This is first a formal identity with the field and mark topologies
specified below. Its principal coefficient \(\mathcal P_0\) is the
analytic phase constructed in [P].

**Theorem.** On fixed smaller disks there are \(M,C>0\) such that
every coefficient in (1) is holomorphic and
\[
       \|\mathcal P_a\|\le M C^a a!\qquad(a\ge0).
 \tag{2}
\]
The disks are independent of \(a\). If \(\mathbf t=hm\), and a
monomial of the original logarithm has quantum order \(j\), equal
creation and differentiation degree \(d\), and clock degree \(b\),
its coefficient satisfies
\[
 \left|[h^j Z^\gamma P^\kappa m^\beta]\log S_h(Z,P,hm)\right|
 \le M C_1^{\,j+d+b+1}(j+1-d-b)!,
 \quad |\gamma|=|\kappa|=d,\quad |\beta|=b.
 \tag{3}
\]
It vanishes when \(j+1-d-b<0\). The source's exact clock filtration
also gives \(b\le j\). Coefficients in (3) are bounded uniformly on
the smaller meridian disk.

The same conclusion (2) holds for the logarithm after the regular
hard contraction used in [P, Section 5]. Its rank-one soft pole is
not included in that contraction. Thus this theorem does not sum
the soft moment functional or the original trace.

We prove a common-disk estimate, not merely a separate estimate for
each polynomial coefficient. The series in \(h\) need not converge.

## 2. Literal entry logarithms and Bernoulli deficiency

Divide each literal crossing summand by its classical summand, as
in [H]. Its logarithm is
\[
             \sum_{j\ge1}h^j v_j(N),\qquad \deg v_j\le j+1,
 \tag{4}
\]
where \(N\) denotes the three nonnegative transfer/input coordinates
of the positive or negative kernel. We require the following
quantitative refinement:
\[
             |[N^\gamma]v_j|\le C^{j+|\gamma|+1}
                                      (j+1-|\gamma|)!.
 \tag{5}
\]
All coefficients here are holomorphic on a common meridian disk.

Here is a direct proof from [F, (2)]. The analytic functions
\[
 f(s)=\log\frac{e^s-1}{s},\qquad
 g_\pm(Y,s)=\log\frac{1-Y^{\pm1}e^s}{1-Y^{\pm1}}
 \tag{6}
\]
have value zero at \(s=0\). Their Taylor coefficients on buffered
disks are bounded by \(C^{j+1}\). Factorial units and color-product
logarithms are sums of these coefficients times powers of integer
linear endpoints. Their endpoint offsets are fixed integers.

For precision define Bernoulli polynomials by the convergent germ
\[
 \frac{t e^{ct}}{e^t-1}=\sum_{a\ge0}B_a(c)\frac{t^a}{a!}.
 \tag{7}
\]
For every one of the finitely many fixed offsets \(c\),
\(|B_a(c)|\le C^{a+1}a!\). Summing a geometric exponential and
comparing its \(t^j\) coefficient gives the exact power-sum identity
\[
 \sum_{r=0}^{L-1}(r+c)^j
  =\frac{B_{j+1}(L+c)-B_{j+1}(c)}{j+1}.
 \tag{8}
\]
The coefficient of \(L^d\), \(1\le d\le j+1\), is
\(\binom{j+1}{d}B_{j+1-d}(c)/(j+1)\).
It has the bound \(C^{j+1}(j+1-d)!\).
An interval is a difference of two such expressions. Replacing its
endpoints by fixed integer linear forms in \(N\) costs at most an
additional exponential in \(d\).

These are exactly the factorial and color intervals of the two
signed entries. The fixed-\(Y\) substitution
\(x=Y^{1/2}e^{-h/2}\) only changes their fixed endpoint offsets.
The \(Q\)-monomials give quadratic polynomials at order one;
the \(x\)-power drift gives linear polynomials at that order.
These also obey (5). Thus all literal terms, including the lower
degrees, satisfy (5); no endpoint correction has been dropped.

Regroup (4) after writing the scaled indices as \(s=hN\):
\[
 \sum_{j\ge1}h^jv_j(N)=
       \sum_{a\ge0}h^{a-1}V_a(s).
 \tag{9}
\]
A degree \(d\) term on the right has \(j=a+d-1\).
The bound (5), and the at-most-exponential number of monomials of
degree \(d\) in the fixed dimension, imply on a common small
\(s\)-polydisk
\[
             \|V_a\|\le M C^a a!.
 \tag{10}
\]
The principal \(V_0=O(s^2)\) is precisely the analytic top potential
of [P, (15)--(16)]. Formula (10) also controls every lower-defect
term. At any fixed original \(h\)-order, (9) recovers the finite
polynomial (4).

## 3. A Gaussian closure estimate with quantum defects

We first prove an analytic Wick lemma. Let \(K\) be a symmetric
complex matrix, with no invertibility requirement. Allow it and
all coefficients to depend holomorphically on parameters in fixed
disks. Suppose \(P_0\) is analytic, and \(P_a\), \(a\ge1\), obey
\(\|P_a\|\le M C^a a!\) on a common field disk. Consider
\[
 Z_h(q)=\mathbb E_{hK}
   \exp\left(\frac{P_0(q+X)}h+
                   \sum_{a\ge1}h^{a-1}P_a(q+X)\right).
 \tag{11}
\]
Assume the small stationary solution
\[
       u=q+K\nabla P_0(u)
 \tag{12}
\]
exists analytically, and \(I-KP_0''(u)\) is a unit on the disks.
The formal expansions below are made either where the classical
quadratic part vanishes, or parameter-adically where its closed
chains are finite at each parameter degree. Quadratic resummation
then gives the analytic continuation on smaller disks.

The exact Gaussian translation identity, checked on exponential
generators and requiring no \(K^{-1}\), gives (11) as
\[
 e^{F_0(q)/h}\,
 \mathbb E_{hK}\exp\left(
 \frac{P_0(u+X)-P_0(u)-g\cdot X}{h}
       +\sum_{a\ge1}h^{a-1}P_a(u+X)\right),
 \quad
 g=\nabla P_0(u),\quad
 F_0=P_0(u)-\tfrac12g^TKg.
 \tag{13}
\]
Absorb \(H=P_0''(u)\) exactly. The factor and new covariance are
\[
 J=\det(I-KH)^{-1/2},\qquad
                  K_{\rm eff}=(I-KH)^{-1}K .
 \tag{14}
\]
The square-root branch is the one obtained by formal quadratic
expansion. To verify (14), insert an additional generator
\(e^{t\cdot X}\) and replace \(H\) by \(\lambda H\).
Wick integration by parts gives
\((I-\lambda KH)\nabla_t Z=hKt\,Z\).
Thus its \(t\)-dependent factor is
\(\exp(h t^TK_{\rm eff}(\lambda)t/2)\).
At \(t=0\), differentiation in \(\lambda\) gives
\(\partial_\lambda\log Z=\tfrac12\operatorname{Tr}
(H K_{\rm eff}(\lambda))\).
Integration from zero gives the determinant in (14).
These are formal generator identities without a \(K^{-1}\);
their analytic matrix expressions supply the resummation.
The remaining principal potential \(R_0(X)\) has order at least
three in \(X\).

Split the constants \(P_a(u)\), \(a\ge1\), out of the logarithm.
The residual vertices have labels \((a,q)\), where \(q\ge1\) is
their field degree, \(a\ge0\), and \(a=0\) requires \(q\ge3\).
By buffered Cauchy estimates their Taylor coefficients have bounds
\[
                         M C^{a+q}a!.
 \tag{15}
\]
The bound for \(a=0\) is the ordinary analytic bound for \(R_0\).

The cumulant identity retains exactly connected Wick graphs.
For a connected vacuum graph with \(v\) vertices and \(e\) edges,
its contribution to the coefficient of \(h^{\delta-1}\) satisfies
\[
 \delta=\sum_i a_i+e-v+1,\qquad
 g:=e-v+1\ge0,\qquad
 \sum_i(q_i+2a_i-2)=2\delta-2.
 \tag{16}
\]
Each summand in the last expression is at least one. Consequently
\[
       v\le2\delta-2,\qquad e\le3\delta-3,\qquad
                              \sum_i a_i\le\delta.
 \tag{17}
\]
In particular all residual contributions have \(\delta\ge2\).
The constant terms and \(\log J\) supply the separately controlled
lower cases.

We give the factorial count explicitly. Expanding the exponential
with ordered vertices contributes \(1/v!\). Ignoring the
connectedness restriction only enlarges the absolute pairing count,
which is at most
\[
       \frac{(2e)!}{2^e e!\,v!}\le4^e g!.
 \tag{18}
\]
For \(e\ge v\), use
\(\binom{2e}{e}\le4^e\) and
\(e!/v!=\binom ev(e-v)!\le2^e(e-v)!\);
the sharper intermediate \(2^e e!/v!\) gives (18).
For \(e=v-1\), that intermediate is \(2^e/v\), also sufficient.
Multiplying (18) by the vertex factorials in (15) gives
\[
                       g!\prod_i a_i!\le\delta!.
 \tag{19}
\]
This is just the integer multinomial inequality, since
\(g+\sum a_i=\delta\).

The remaining enumeration costs only an exponential in \(\delta\).
Indeed the positive integers \(q_i+2a_i-2\) form a composition of
\(2\delta-2\). Given one such integer \(c_i\), there are at most
\(c_i+2\le3^{c_i}\) permitted pairs \((a_i,q_i)\).
The total field degree \(2e\) is at most \(6\delta-6\).
Field colors, coefficient factors and bounded covariance entries
therefore also cost at most \(C^\delta\). These estimates prove
\[
       \log Z_h=h^{-1}F_0+\sum_{\delta\ge1}h^{\delta-1}F_\delta,
       \qquad \|F_\delta\|\le M' C'^\delta\delta!
 \tag{20}
\]
on smaller common disks. The graph sums are finite at each defect
after the analytic quadratic resummation. They consequently define
holomorphic functions and justify the stated uniform bound.
No estimate of an oscillatory or positive Gaussian integral is used.

## 4. Poisson closure at zero means

The local kernels of [H] are exact Poisson expectations of (9),
with means \(U/h\). A diagonal occupation mean may vanish, so it
cannot be used as a denominator.

Let \(u=U\exp(\nabla V_0(u))\), \(g=\nabla V_0(u)\), and let \(F_0\)
be the analytic entropy expression of [P, (11)].
Poisson exponential reweighting gives exactly
\[
 Z_h=e^{F_0/h}\,
 \mathbb E_{u/h}\exp\left(
 \frac{V_0(hN)-V_0(u)-g\cdot(hN-u)}h
             +\sum_{a\ge1}h^{a-1}V_a(hN)\right).
 \tag{21}
\]
This is first a coefficientwise identity. The implicit \(u(U)\)
is analytic even on every zero-coordinate face.

Put \(X=hN-u\). Its centered moment generator is
\[
     \mathbb E e^{J\cdot X}
       =\exp\left(\sum_i\frac{u_i(e^{hJ_i}-1-hJ_i)}h\right).
 \tag{22}
\]
Use two sets of Wick variables \(X,\Xi\), with the constant
symmetric cross covariance
\[
                     K_\times=\begin{pmatrix}0&I\\I&0\end{pmatrix}.
 \tag{23}
\]
For every polynomial \(f\), direct differentiation of its finite
Taylor expansion proves
\[
 \mathbb E_{u/h}f(hN-u)
 =\mathbb E_{hK_\times}
       f(X)\exp\left(\sum_i u_i(e^{\Xi_i}-1-\Xi_i)/h\right).
 \tag{24}
\]
Indeed the right side applies
\(\exp(\sum_{k\ge2,i}u_i h^{k-1}\partial_{X_i}^k/k!)\)
to \(f\) at zero, exactly (22). This proves the required identity
for the formal exponential in (21) coefficientwise as well.

Thus its residual expectation is the Gaussian construction with
principal potential
\[
 R_u(X)+\sum_i u_i(e^{\Xi_i}-1-\Xi_i),\qquad
 R_u(X)=V_0(u+X)-V_0(u)-g\cdot X,
 \tag{25}
\]
and quantum defect potentials \(V_a(u+X)\). The stationary mean
is zero. Its quadratic Hessian is
\(\operatorname{diag}(V_0''(u),\operatorname{diag}u)\).
At \(u=0\), its product with \(K_\times\) is nilpotent, so the
determinant in (14) is one. More generally that determinant is
\[
                         \det(I-\operatorname{diag}(u)V_0''(u)).
 \tag{26}
\]
It remains a unit on a fixed small \(U\)-disk.

There is no formal finiteness gap at this nonzero quadratic
Hessian: each closed pre-resummation quadratic chain contains a
factor \(u_i\). At fixed \(U\)-degree only finitely many such
chains occur. Equations (14) and (26) sum them analytically.
Afterwards the residual principal vertices are cubic, and (10)
supplies exactly the quantum factorial bounds required in (15).
The estimate (20) therefore holds uniformly including \(U_i=0\).
No inverse of an occupation, a Poisson covariance, or a field
coordinate has appeared.

## 5. The finite word, marks, and the regular hard contraction

The Poisson means of each actual kernel are the three bilinear
forms displayed in [H] and [P]. On scaled fields they are \(U/h\).
Section 4 gives its ordinary logarithm with the estimate (20).
Dividing by the classical kernel and making the invertible linear
substitution for \(R_\pm\Gamma(L_\pm)^{-1}\) changes no deficiency.
The principal relative phase is quartic at zero marks, as in [P].

The scaled normal product is exactly
\[
 A\star_h B=
 \left.e^{h\partial_r\cdot\partial_s}
                   A(Z,P+r)B(Z+s,P)\right|_{r=s=0}.
 \tag{27}
\]
Regard external fields as additional mean coordinates with zero
covariance. Then (27) is the Gaussian lemma with the cross
covariance in the internal \(r,s\) variables. Its principal
implicit problem is precisely [P, (26)]. At zero fields and marks,
the principal Hessian vanishes. On small disks its quadratic
inverse is a unit. Sections 3--4 therefore prove (2) through every
one of the finitely many compositions.

An independent stage mark has exact scaled normal symbol
\[
             \exp\bigl(Z^T(M(\mathbf t)-I)P/h\bigr).
 \tag{28}
\]
Its principal phase is quadratic and vanishes with \(\mathbf t\).
Use the mark-adic topology before analytic quadratic resummation;
every extra quadratic chain then has positive mark degree.
All coefficients after resummation are bounded on common small
mark disks. Thus the same finite-composition argument keeps
independent marks throughout.

The original pivot is a substitution with matrix \(I+O(h)\).
Its scaled logarithm has analytic coefficients at nonnegative
powers of \(h\), and satisfies (2). The scalar framing correction
does also. The fixed scalar \(x_0^c\) remains external as before.
The highest-cut projector remains in the same right-hand matrix
as [P]; it is not part of an invertible conjugation.

For the optional regular hard contraction, [P, (28)--(29)]
provides a holomorphic covariance \(G(Y)\), represented by the
symmetric block matrix
\(\begin{pmatrix}0&G^T\\G&0\end{pmatrix}\).
The principal phase is again quartic at zero marks, and its
stationary/quadratic equations are analytic on smaller disks.
Section 3 proves (2) for that logarithm as well. The singular
soft contraction \(uv^T/z\) has not been used in this estimate.

In particular substitute the soft means \(Z=vA,\ P=uB_s\), as in
[P]. Every hard logarithm coefficient is balanced and is therefore
an analytic function of \(x=AB_s\). If its bound on
\(|A|,|B_s|<r\) is \(MC^a a!\), Cauchy bounds its \(x^d\)
coefficient by \(MC^a a!r^{-2d}\). Summation on
\(|x|<r^2/2\) gives the explicit common-disk conclusion
\[
 \log\mathcal H_{\rm scaled}
    =\sum_{a\ge0}h^{a-1}\Psi_a(z,x,\mathbf t),\qquad
 \sup_{z,x,\mathbf t}|\Psi_a|\le 2MC^a a!.
 \tag{28a}
\]
The meridian and independent-mark disks here are fixed smaller
disks, independent of \(a\). This controls the entire analytic
coefficient in \(x\), not just each of its Taylor coefficients.

Finally apply Cauchy extraction to (2) in fields and marks.
A balanced field monomial of degree \(d\) and mark degree \(b\)
has bound \(M C^{a+2d+b}a!\). Substitute \(\mathbf t=hm\) and
undo the field scaling. Its original quantum order is
\[
                         j=a-1+b+d .
 \tag{29}
\]
This gives exactly (3), with constants enlarged once. Each
fixed specialization to matching-lattice clocks costs only an
additional exponential in \(b\). The inequality \(b\le j\) is
also the literal mark filtration: each original clock factor
starts with \(h m\), before any symbol operation. Formal
coefficient identities preserve it.

## 6. Scope and complete proof directs

This supplies factorial-deficiency estimates for the full ordinary
symbol logarithm and its regular hard contraction, while retaining
the original operations. It proves no convergence of the \(h\)-series,
quantum amplitude or soft moment sum. In particular it does not
authorize an infinite Ward operator on a continued Borel source,
identify the actual moving marked minor, or select a physical cycle.

| Label | Complete proof direct | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| H | notes/research_actual_source_natural_log_filtration.md | 98c371fe71a210e9d886e30d60a487a3fe46599f1814c1b69229d829a1eb6f88 |
| P | notes/research_actual_analytic_principal_phase.md | 9ae7b5df2dbd955ee6ac4580590d9f21d1b1750bcdd6c5085e7322251ab70bcb |

F and H supply the literal entry, kernel, and finite-word identities.
P supplies the analytic principal implicit solutions and the original
hard covariance. The Bernoulli estimate, Gaussian quantum-defect count,
zero-mean Poisson adapter and full coefficient bounds are proved above.
Only written mathematics and source-text/hash operations were used.
Frozen proofs and public manuscripts are unchanged.
