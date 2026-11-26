# A polynomial horn for the actual canonical Borel source

Private written proof, 18 November 2026.

The continuation theorem [J] retains the whole canonical source but
allows its transverse disk to shrink with the Borel path. Here the
same exact hierarchy gives a quantitative disk along unbounded rays.
The disk shrinks only as a fixed power of the Borel distance. This
does not give a full Laplace ray at a fixed nonzero meridian
displacement.

## 1. The actual source and the assertion

Retain all hypotheses and conventions of [J]. In particular,
\(h=\log Q\), \(z=Y-\alpha\), and \(\alpha\) is a simple Alexander
root. The supplied actual finite-shift annihilator has a transverse
abelian/nonabelian node. Its constants are
\[
 r=\Delta_K'(\alpha)^{-1},\qquad
 A=\frac{\alpha^2}{2}P_{LL}(\alpha,1),\qquad
 B=\alpha P_{YL}(\alpha,1),\qquad \eta_*=\frac{B}{2A}.
 \tag{1}
\]
The original canonical germ is
\[
 b(z,\eta)=\sum_{k\ge0}b_k(\eta)z^k
 =\sum_{j\ge0}z^{2j+1}W_j(\alpha+z)\frac{\eta^j}{j!}.
 \tag{2}
\]
It starts with
\(b(0,\eta)=r(1-\eta/\eta_*)^{-1/2}\).

Choose a sheet by a fixed compact path from this germ, avoiding
\(0,\eta_*\) after its starting segment. Continue to a circle of
radius \(R_0>2|\eta_*|+1\), and then along outward rays whose angles
lie in a fixed compact interval. The connecting arcs on that circle
are chosen in one fixed lifted angular interval; arbitrary repeated
winding is not included in a single uniform family. The path lengths
before the outward rays are uniformly bounded, and those paths stay
a positive distance from the two punctures after the initial segment.

**Theorem.** There are constants \(C,D>0\) and a fixed
\(\kappa\ge2\), depending on the source and chosen path family but
not on \(k\) or the distance along a ray, such that
\[
 |b_k(\eta)|+\frac{(1+|\eta|)|b_k'(\eta)|}{k+1}
       \le C D^k(1+|\eta|)^{\kappa(k+1)}.
 \tag{3}
\]
Consequently the continued canonical source is jointly holomorphic
on neighborhoods in the horn
\[
             D|z|(1+|\eta|)^\kappa<1,
 \tag{4}
\]
on the chosen sheet. On its smaller closed horn,
\[
 D|z|(1+|\eta|)^\kappa\le\frac12,
 \qquad |b(z,\eta)|\le2C(1+|\eta|)^\kappa.
 \tag{5}
\]
At the finite connecting portions these statements mean their
corresponding continuation neighborhoods. Constants can be enlarged
to include them.

The radius in (4) is positive at every finite Borel distance, but
tends to zero at infinity. No fixed-\(z\) summability assertion is
part of the theorem.

## 2. The exact hierarchy retained from the source

We recall the precise identities of [J] used in the estimate.
The finite shifts give coefficients \(a_{n\ell}(z)\) satisfying
\[
 |[z^v]a_{n\ell}|\le C_0 H^n Z^v/\ell!,
 \qquad 0\le\ell\le n.
 \tag{6}
\]
In a lower term of transverse order \(s\ge1\),
\[
 s=2n-\ell-2+v,\qquad n\le s+2,\qquad v\le s+1.
 \tag{7}
\]
With \(p=k-s\), its contribution to the \(k\)-th equation is
\[
 [z^v]a_{n\ell}\ I^{n-1}P_\ell(p-2\theta)b_p,
 \quad
 I f=\int_0^\eta f(\xi)\,d\xi,\quad
 \theta=\eta\partial_\eta,\quad
 P_\ell(u)=\prod_{i=1}^{\ell}(u-i).
 \tag{8}
\]
Every primitive is along the entire chosen continued path, beginning
in the canonical germ. In particular its history is retained.

Put \(a=n-1\). The exact normal ordering is
\[
 I^aP_\ell(p-2\theta)=
 \sum_{q=0}^{\ell}d_q\eta^qI^{a-q},\qquad
 \frac{|d_q|}{\ell!}
 \le
 \frac{2^q(p+C_*n)^{\ell-q}}{q!(\ell-q)!}.
 \tag{9}
\]
The only negative primitive allowed is \(I^{-1}=\partial_\eta\),
occurring when \(q=\ell=n=a+1\). Thus (9) has no omitted endpoint
term or higher derivative. This follows in [J] by commuting \(I^a\)
past \(\theta\), before expanding in the falling powers of \(\theta\).

Let \(F_k\) be minus the sum of all terms (8), so \(F_0=0\), and put
\[
 G_k=(B-2A\eta)b_k+A(k+1)I b_k.
 \tag{10}
\]
The exact leading system, with its canonical initial values, is
\[
 \frac d{d\eta}\binom{b_k}{G_k}
 =
 \begin{pmatrix}
 -A(k-1)/(B-2A\eta)&k/[2\eta(B-2A\eta)]\\
 0&k/(2\eta)
 \end{pmatrix}\binom{b_k}{G_k}
 -
 \binom{1/[2\eta(B-2A\eta)]}{1/(2\eta)}F_k.
 \tag{11}
\]
No new solution is chosen when this system is used.

## 3. Polynomial weights pay the full source forcing

Parameterize a path, including its initial segment from zero, by arc
length \(t\ge0\). Its outward part is a straight ray. Uniformly over
the chosen family there is \(C_1\) such that
\[
 |\eta(t)|\le C_1(1+t),\qquad
 1+t\le C_1(1+|\eta(t)|).
 \tag{12}
\]
The second inequality on the finite connecting part follows by
enlarging \(C_1\). On the ray it follows directly from its bounded
initial length.

For a finite terminal time \(T\), define
\[
 M_p(T)=\sup_{0\le t\le T}(1+t)^{-\kappa(p+1)}
 \max\left\{|b_p(\eta(t))|,
       \frac{(1+t)|b_p'(\eta(t))|}{p+1}\right\}.
 \tag{13}
\]
The derivative weight \(1+t\) is essential for the \(I^{-1}\)
term in (9).

For \(u\ge1\), the exact continued primitive is
\[
 I^u b_p(\eta(t))=
 \frac1{(u-1)!}\int_0^t
 [\eta(t)-\eta(s)]^{u-1}b_p(\eta(s))\eta'(s)\,ds.
 \tag{14}
\]
Since \(|\eta(t)-\eta(s)|\le t-s\), put
\(\lambda=\kappa(p+1)>0\). Extension of the positive majorant
integral from \(1\le1+s\le1+t\) to \(0\le1+s\le1+t\) gives
\[
\begin{split}
 |I^u b_p(\eta(t))|
 &\le M_p(T)(1+t)^{\lambda+u}
       \frac{\Gamma(\lambda+1)}{\Gamma(\lambda+u+1)}\\
 &\le M_p(T)\frac{(1+t)^{\lambda+u}}{\lambda^u}.
\end{split}
 \tag{15}
\]
Only the elementary beta integral is used here. The gamma quotient
is \(\prod_{j=1}^u(\lambda+j)^{-1}\), so the last inequality is
valid for every integer \(u\ge1\).

For \(q\le a\), the term in (9) has time power
\((1+t)^{\lambda+q+a-q}=(1+t)^{\lambda+a}\), apart from
the factor \(C_1^q\). For \(q=a+1\), (13) bounds the derivative
by \((p+1)M_p(T)(1+t)^{\lambda-1}\), and the total time power
is again \(\lambda+a\). Thus the original derivative endpoint
has exactly the same time budget as the primitives.

In the weight of the output \(k=p+s\), the remaining time power is
\[
                   a-\kappa s=n-1-\kappa s\le0
                   \quad\text{if }\kappa\ge2,
 \tag{16}
\]
because \(n-1\le s+1\le2s\). All histories in (14) obey this
estimate, including the compact detours.

The remaining numerical estimate is the one in [J], now independent
of \(T\). Explicitly, combine (6) and (9) with (15). Factor
\[
 p+C_*n\le(p+1)\bigl(1+C_*n/(p+1)\bigr)
\]
and use \(v\le s+1,\ n\le s+2\), together with
\[
 \frac{(1+C_*n/(p+1))^j}{j!}\le e^{1+C_*n}.
 \tag{17}
\]
The remaining power of \(p+1\) is at most
\(\ell-a\le1\); the sum of \((2C_1)^q/q!\) is bounded.
The sole derivative case \(q=\ell=n\) has the same bound.
Absorbing the polynomial count of \((n,\ell,v)\) into an
exponential gives constants independent of \(T\):
\[
 \sup_{t\le T}(1+t)^{-\kappa(k+1)}|F_k(\eta(t))|
 \le C_2\sum_{s=1}^k D_0^s(k-s+1)M_{k-s}(T).
 \tag{18}
\]

## 4. The leading system has a uniform gain

After the known initial segment, (11), including the factor
\(\eta'(t)\), has a matrix norm bounded by
\[
                  C_3(k+1)/(1+t)
 \tag{19}
\]
and a forcing coefficient bounded by \(C_3/(1+t)\).
On the compact connecting part this follows from avoidance of the
two punctures. On each outward ray it follows from the displayed
rational coefficients in (11). The constants are uniform over the
fixed angular interval.

Choose \(\kappa>\max(2,C_3+1)\). The fundamental matrix between
times \(s\le t\), after the initial segment, is bounded by
\[
                  \left(\frac{1+t}{1+s}\right)^{C_3(k+1)}.
 \tag{20}
\]
Variation of constants in the weight (13) therefore gives the forced
vector a bound
\[
 \frac{C_4}{k+1}
    \sup_{t\le T}(1+t)^{-\kappa(k+1)}|F_k(\eta(t))|.
 \tag{21}
\]
Indeed the remaining scalar integral is bounded by
\[
 \frac1{(1+t)^{(\kappa-C_3)(k+1)}}
 \int^{t}(1+s)^{(\kappa-C_3)(k+1)-1}\,ds
 \le\frac1{(\kappa-C_3)(k+1)}.
\]
The first row of (11) gives the same bound for
\((1+t)b_k'/(k+1)\).

The initial joint germ bounds its \(b_k,b_k'\) exponentially in \(k\).
Equation (10) bounds its initial \(G_k\) by the same exponential
times \(k+1\), which can be absorbed into another fixed exponential.
The homogeneous term in (20) preserves that bound. Combining
(18)--(21) proves
\[
 M_k(T)\le C_5D_1^k+C_5\sum_{s=1}^kD_0^sM_{k-s}(T).
 \tag{22}
\]
Every constant is independent of \(T\). Induction in \(k\) gives
\(M_k(T)\le C_6D_2^k\). Since each finite path continuation is the
canonical one of [J], letting \(T\) increase gives this bound on the
entire ray. Equation (12), with constants absorbed into \(C,D\),
now proves (3).

Nearby rays and short terminal continuations have the same bounds
with enlarged constants. Thus the estimates hold on neighborhoods,
not only path values. Summing the normally convergent \(z\)-series
proves (4)--(5) and identifies it with the same canonical continuation.

## 5. The finite cutoff scale and the unpaid operation

For small fixed \(z\ne0\), (5) allows a Borel cutoff of size
\[
 |\eta_{\rm cut}|=R(z)=c|z|^{-1/\kappa},\qquad
 \xi_{\rm cut}=z^2\eta_{\rm cut},\qquad
 |\xi_{\rm cut}|=c|z|^{2-1/\kappa},
 \tag{23}
\]
with a sufficiently small fixed \(c>0\). Here \(\xi=z^2\eta\)
is the original \(h\)-Borel variable; the direction and continuation
sheet remain specified. In particular
\(|\xi_{\rm cut}|/|z|^2\to\infty\) as \(z\to0\).
This is a scale comparison only. No truncated Laplace transform
or residual equation is asserted here.

At any fixed nonzero \(z\), the ray eventually exits (4).
Consequently this theorem does not produce an exponentially bounded
Borel transform along a full fixed-\(z\) ray, a Laplace sum, or an
identification with the original finite-color values. Nor does it
locate a nearby singularity or determine a selected geometric
exponential. Those conclusions require a further estimate or an
actual source-preserving finite-contour operation.

The only proof direct is:

| Label | Complete source | SHA256 |
|---|---|---|
| J | notes/research_classical_verma_borel_joint_continuation.md | 67cbb4c1577af04336b53985e867f6d2adc7e184c6d4276c53a0888f57d8ded8 |

J supplies the actual shift coefficients, exact normal ordering,
canonical hierarchy and finite-path joint continuation. The
polynomial weights, uniform infinite-ray estimate, and cutoff scale
are proved here. No external proof, mathematical program, test, or
build is used. Frozen proofs and public manuscripts are unchanged.
