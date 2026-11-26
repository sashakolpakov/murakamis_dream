# Exponential continuation bounds for polynomial-log Cauchy densities

Private written proof, 18 November 2026.

A polynomial density on one segment, together with finitely many
endpoint derivatives, has a Cauchy transform that is rational plus a
polynomial times a logarithm. Its norm on a fixed outer circle
controls its norm on every fixed continued compact set with a cost
exponential in the polynomial degree and endpoint pole orders.
There is no degree-times-log-degree loss.

This is an estimate for the displayed function class. It does not
assert that every transverse coefficient of the marked knot source
belongs to that class, or that such a class is closed under all the
source operations.

## 1. The normalized function class

First put the two endpoints at zero and one. Let
\[
 \mathcal L(z)=\log(1-z^{-1})
             =-\sum_{m\ge1}\frac{z^{-m}}m,\qquad |z|>1.
 \tag{1}
\]
Continue this specified branch on the universal cover of
\(\mathbb C\setminus\{0,1\}\). Consider
\[
 F(z)=\frac{A(z)+B(z)\mathcal L(z)}
                 {z^{r_0}(z-1)^{r_1}},
 \qquad
 \deg A,\deg B\le d,\quad r_0,r_1,d\in\mathbb Z_{\ge0}.
 \tag{2}
\]
The zero polynomial is allowed. The degrees in (2) are upper bounds,
so no minimal representation is needed.

Fix \(R>1\). Let \(K\) be a compact set on a specified continuation
cover, disjoint from the two endpoints, and put
\[
 \begin{split}
 M&=\sup_{|z|=R}|F(z)|,\qquad
 \lambda_R=-\log(1-R^{-1}),\\
 d_0&=\inf_K|z|>0,\qquad d_1=\inf_K|z-1|>0,\\
 L_K&=\sup_K|\mathcal L(z)|<\infty,\qquad
 q_K=\max\left(1,\frac{\sup_K|z|}{R}\right),\\
 C_R&=2^{14}R^2(1+\lambda_R).
 \end{split}
 \tag{3}
\]
The norm defining \(M\) uses the original outer branch (1).
Projections to the \(z\)-plane are understood in the other suprema.

**Theorem.** Every function (2) satisfies
\[
 \boxed{\displaystyle
 \sup_K|F|
 \le M(1+L_K)(2q_K C_R)^{d+1}
             (R/d_0)^{r_0}((R+1)/d_1)^{r_1}.}
 \tag{4}
\]
In particular, for fixed \(R,K\), this is
\(M C_K^{\,d+r_0+r_1+1}\) after increasing a fixed constant \(C_K\).
No bound on the separate coefficients of \(A\) or \(B\) is assumed.
Their possible cancellation on the outer circle is included in (4).

## 2. A Hilbert inverse with an exponential bound

For \(n\ge1\) let
\[
 H_{ij}=\frac1{i+j+1},\qquad 0\le i,j<n.
 \tag{5}
\]
We derive its inverse rather than import an asymptotic condition
number. To solve \(H b=e_m\), define
\[
 D(z)=\prod_{j=0}^{n-1}(z+j+1),\qquad
 \Lambda_m(z)=\prod_{\substack{0\le i<n\\i\ne m}}
                         \frac{z-i}{m-i}.
 \tag{6}
\]
The rational function
\[
 \frac{D(m)\Lambda_m(z)}{D(z)}
                    =\sum_{j=0}^{n-1}\frac{b_j}{z+j+1}
 \tag{7}
\]
has value \(\mathbf1_{i=m}\) at \(z=i\). Its numerator has degree
at most \(n-1\), so its partial fractions contain no polynomial part.
Taking residues at \(-j-1\) proves invertibility and gives
\[
 (H^{-1})_{jm}
 =(-1)^{j+m}(j+m+1)
   \binom{n+j}{n-m-1}
   \binom{n+m}{n-j-1}
   \binom{j+m}{j}^{\!2}.
 \tag{8}
\]
For example the magnitude directly from (7) is
\[
 \frac{(n+m)!(n+j)!}
 {(m!)^2(j!)^2(n-1-m)!(n-1-j)!(j+m+1)},
 \tag{9}
\]
which equals the magnitude in (8); the residue sign is
\((-1)^{j+m}\).

Every binomial coefficient \(\binom ab\) is at most \(2^a\), by
the binomial expansion of \((1+1)^a\). Hence each entry of (8)
has magnitude at most \(2n\,2^{8n}\). Summing a row and using
\(2n^2\le2^{3n}\) gives the deliberately coarse bound
\[
                         \|H^{-1}\|_{\infty\to\infty}
                              \le2^{11n}.
 \tag{10}
\]
All estimates are uniform in \(n\). The factorials in (9) have
combined into binomial coefficients before any bound is taken.

## 3. Recovering the logarithmic and polynomial coefficients

Multiply (2) by its displayed denominator and write
\[
 G(z)=z^{r_0}(z-1)^{r_1}F(z)=A(z)+B(z)\mathcal L(z),\qquad
 M_0=M R^{r_0}(R+1)^{r_1}.
 \tag{11}
\]
Then \(\sup_{|z|=R}|G|\le M_0\).
Write \(B(z)=\sum_{j=0}^d b_jz^j\), and let \(c_m\) be the
coefficient of \(z^{-m}\) in the Laurent expansion of \(G\) outside
the unit disk. The polynomial \(A\) contributes none of them. By
(1),
\[
 c_m=-\sum_{j=0}^d\frac{b_j}{m+j},\qquad m\ge1.
 \tag{12}
\]
The Laurent coefficient integral gives
\[
 c_m=\frac1{2\pi i}\int_{|z|=R}G(z)z^{m-1}\,dz,\qquad
                              |c_m|\le M_0R^m.
 \tag{13}
\]
Set \(n=d+1\) and use only \(m=1,\ldots,n\). This is exactly
the system (5), with right side \(-c_{i+1}\). Thus
\[
              \max_j|b_j|\le2^{11n}M_0R^n.
 \tag{14}
\]
Since \(n\le2^n\) and \(n+d\le2n\),
\[
 \sup_{|z|=R}|B(z)|
 \le n\,2^{11n}M_0R^{n+d}
 \le M_0(2^{12}R^2)^n.
 \tag{15}
\]
On the same circle, (1) gives \(|\mathcal L|\le\lambda_R\).
Consequently (11) and (15) imply
\[
             \sup_{|z|=R}|A(z)|,\ 
             \sup_{|z|=R}|B(z)|\le M_0 C_R^n .
 \tag{16}
\]
This also shows that the representation has no invisible kernel:
if \(M=0\), first (12) gives \(B=0\), and then \(A=0\).

For either polynomial \(V=A,B\), Cauchy's coefficient estimate
on the circle of radius \(R\) gives
\[
 \sup_K|V|
 \le n\sup_{|z|=R}|V|\,
             \max(1,\sup_K|z|/R)^d
 \le M_0(2q_K C_R)^n.
 \tag{17}
\]
Divide by the two endpoint factors and use the bounded continued
logarithm on \(K\). Equations (11) and (17) prove (4).
Only finitely many exterior moments were needed; their number is
linear in the displayed degree.

## 4. Segment densities and endpoint derivatives

Let \(P(t)\) be a polynomial of degree at most \(q\), and let
the initial segment be the straight path from zero to one. Its
Cauchy transform is
\[
 \begin{split}
 \int_0^1\frac{P(t)}{z-t}\,dt
  &=-P(z)\mathcal L(z)
       -\int_0^1\frac{P(z)-P(t)}{z-t}\,dt .
 \end{split}
 \tag{18}
\]
The last integral is a polynomial of degree at most \(q-1\)
and is zero when \(q=0\). Formula (18) follows by polynomial
division and \(\int_0^1(z-t)^{-1}dt=-\mathcal L(z)\) on the
outer branch.

The normalized endpoint derivative of order \(j\), acting on
the Cauchy kernel, is
\[
 \left.\frac1{j!}\partial_t^j\frac1{z-t}\right|_{t=e}
                         =\frac1{(z-e)^{j+1}},
                  \qquad e=0,1.
 \tag{19}
\]
Arbitrary unnormalized derivatives are covered as well: their
factorials are simply part of their unrestricted coefficients.
Thus a polynomial-density segment plus endpoint derivatives of
orders less than \(r_0,r_1\) has the form (2), with the safe choice
\[
                              d=r_0+r_1+q.
 \tag{20}
\]
No density or endpoint-coefficient norm is required; the hypothesis
is the norm of the whole Cauchy transform on the outer circle.

More generally one may add a rational function with the same
endpoint pole orders and a polynomial part of degree at most \(g\).
Then \(d=r_0+r_1+\max(q,g)\) is sufficient. This includes the
rational-plus-log class with controlled growth at infinity mentioned
in the statement of the problem.

For endpoints zero and a fixed \(a\ne0\), put \(z=\theta/a\).
If the given outer circle is \(|\theta|=R_\theta>|a|\), use
\(R=R_\theta/|a|>1\). Polynomial degrees and pole orders are
unchanged. Applying (4) to \(F(az)\) proves the same exponential
bound on every fixed continued compact away from \(\{0,a\}\).
Complex \(a\) merely rotates and scales that circle.

The constants are also uniform when \(a\) varies in a compact set
bounded away from zero, the outer circle stays a fixed positive
distance outside all endpoints, the target compacts stay a fixed
positive distance from both endpoints, and the chosen continued
logarithms are uniformly bounded there. No uniformity over
unbounded winding labels is asserted. At \(a=0\) the segment is
absent and the remaining one-endpoint rational estimate is elementary;
this does not assert a uniform two-endpoint decomposition through
that collision.

## 5. Exponential transverse families and scope

Suppose a family indexed by \(k\ge0\) has representations (2) with
\[
 d_k+r_{0,k}+r_{1,k}+1\le C_0(k+1),\qquad
                  \sup_{|z|=R}|F_k|\le M A^k.
 \tag{21}
\]
Here \(C_0,R,A\) are fixed. Equation (4), after replacing each
fixed factor by its maximum with one, gives constants \(M',B\)
depending only on these fixed data and the continued compact such
that
\[
                              \sup_K|F_k|\le M'B^k.
 \tag{22}
\]
For instance take
\[
 \begin{split}
 C_*&=\max(1,\,2q_KC_R,\,R/d_0,\,(R+1)/d_1),\\
 M'&=M(1+L_K)C_*^{C_0},\qquad
 B=A C_*^{C_0}.
 \end{split}
 \tag{23}
\]
If \(A=0\), interpret the trivial vanishing tail separately.
The same estimate on compact neighborhoods gives normal convergence
of a transverse series \(\sum_k s^kF_k\) for a positive \(s\)-radius
after continuation to the fixed chart.

The proof controls cancellations of the density and endpoint terms,
including confluent endpoint orders growing linearly with \(k\).
It does not replace those terms by positive measures, omit the
logarithmic connector, or split its two endpoint monodromies into
independent point evaluations.

The source-theoretic assertion that a particular full marked
transverse family has this bounded-complexity representation is
separate. No such assertion, localization at one endpoint, or
physical scalar lower bound is inferred from (22).

The entire argument is self-contained: polynomial division,
finite rational interpolation, Laurent coefficient integrals and
Cauchy estimates are proved or displayed above. No external
conditioning theorem or mathematical computation is used.
Repository searches found no earlier instance of this particular
large-circle-to-continued-chart estimate. The existing
natural-log-filtration calculation supplies a relevant logarithmic
connector, but is not a proof premise here.

Only written mathematics, source searches and text/hash operations
were used. Frozen notes and public manuscripts are unchanged.
