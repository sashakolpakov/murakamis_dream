# A full-degree generating section with its original source normalization

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The centered Conway basis has a generating polynomial whose finite
quantum-difference equation includes the exact characteristic-polynomial
forcing. At every physical Casimir node it factors into finite products.
This gives a nonzero dilogarithmic approximation on the entire open unit
disk, uniformly through both ends of the physical index range.

The same approximation retains the actual first Casimir normals.
Their proof uses an exact cyclic primitive with a necessary central
correction, rather than differentiation of values interpolated between
the physical nodes. An explicit analytic section is exponentially
accurate in all these physical Hermite coordinates. A separate
small-disk estimate reaches fixed off-spectrum Casimir labels too.
Neither statement identifies the original closing of a general assembled
short component.

## 1. The actual generating polynomial and its terminal equation

Use the full algebra and centered basis of
[the Fourier compiler](research_centered_fourier_conway_compiler.md):
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 p=Q^{-1},\quad \eta=(-1)^d,\quad
 P_N(z)=2T_N(z/2)+2 .
\]
The quotient \(\mathcal H_N=\mathbb C[z]/P_N\) retains first
derivatives at double roots. Its physical nodes are
\[
 c_j=q^{2j+1}+q^{-2j-1},\qquad 0\le j\le d.
\]
The centered basis satisfies
\[
 f_a=N^{-1/2}R^+p_a(z),\qquad p_0=1,
\]
where \(R^+\) is the original invertible positive crossing and
\[
 zp_a=(p^{a+1}-1)p_{a+1}+2q^{-1}p^ap_a+(p^a-1)p_{a-1}
                    \quad(0\le a<d).
 \tag{1}
\]
Here \(p_{-1}=0\); the symbol \(p\) without an index is the root
\(Q^{-1}\), not one of the polynomials. Each \(p_a\) has degree \(a\).
Define
\[
 G_N(t;z)=\sum_{a=0}^{d}p_a(z)t^a,\qquad
 D_N(t)=1-\eta t^N=1+(-1)^Nt^N .
 \tag{2}
\]
Every coefficient in (2) is an ordinary polynomial in \(z\).

For completeness, the terminal relation in (1) has the following
ordinary-polynomial normalization. Put
\[
 \mathcal P_a=(-1)^a(p;p)_a p_a\quad(0\le a\le d).
\]
These are monic. Define the next monic polynomial by the terminal
recurrence, rather than by a vanishing factorial:
\[
 \mathcal P_{\rm term}
   =(z-2q^{-1}p^d)\mathcal P_d-(1-p^d)^2\mathcal P_{d-1}.
\]
The actual endpoint identity for multiplication by \(z\) in the
centered basis shows \(\mathcal P_{\rm term}=0\) in \(\mathcal H_N\).
Its degree is \(N\) and its leading coefficient is one. It is therefore
exactly \(P_N\). Also \((p;p)_d=N\), by factoring \(u^N-1\) at \(u=1\).
Consequently summing (1), including its terminal remainder, gives
\[
 \boxed{\quad
 (1+q^{-1}t)^2G_N(pt;z)-(1+zt+t^2)G_N(t;z)
                  =\frac{(-1)^N}{N}P_N(z)t^N .
 \quad}
 \tag{3}
\]
Indeed the coefficient of \(t^{a+1}\), for \(a<d\), is (1);
the last coefficient is
\[
 (2q^{-1}p^d-z)p_d+(p^d-1)p_{d-1}
       =-\frac{P_N(z)}{(-1)^dN}.
 \tag{4}
\]
No polynomial \(p_N\) has been defined by division by zero.

Let \(b(t,z)=1+zt+t^2\). If \(z=w+w^{-1}\), factoring the finite
products proves the exact cyclic norm identity
\[
 \boxed{\quad
 \prod_{k=0}^{N-1}\frac{b(p^kt,z)}{(1+q^{-1}p^kt)^2}
       =1-\frac{(-1)^NP_N(z)t^N}{D_N(t)^2}.
 \quad}
 \tag{5}
\]
Both sides are polynomial identities after denominators are cleared,
so no choice of \(w\) is needed in the assertion. In the full
nonreduced algebra \(\mathcal H_N\), this norm is one wherever
\(D_N(t)\ne0\). Off that algebraic relation, the forcing in (3)
remains. It cannot be replaced by a homogeneous eigenfunction
equation at an arbitrary geometric Casimir value.

There is a precise local section ambiguity, also in the nonreduced
algebra. In \(\mathcal H_N[[t]]\), the polynomial \(G_N\) is a
formal unit with constant coefficient one and satisfies
\[
       G_N(pt)=\frac{b(t,z)}{(1+q^{-1}t)^2}G_N(t).
 \tag{5a}
\]
If \(F\) is any other formal unit solution with \(F(0)=1\),
then \(F/G_N\) is invariant under \(t\mapsto pt\).
Comparison of coefficients, using that \(p\) is primitive, proves
\[
                   F/G_N\in1+t^N\mathcal H_N[[t^N]].
 \tag{5b}
\]
Conversely every such factor gives another normalized solution.
Multiplication by this group is free and transitive on the normalized
solutions. This is the local section torsor meant here. No
semisimple quotient or general Hilbert 90 theorem is used.

There is also an explicit finite-product analytic cochain. Set
\(a(t,z)=b(t,z)/(1+q^{-1}t)^2\), and anchor all logarithms at zero:
\[
 \mathcal E_N(t,z)=
   \exp\!\left\{\frac1N\sum_{k=0}^{d}k\log a(p^kt,z)\right\}.
 \tag{5c}
\]
Reindexing the finite sum proves
\[
 \frac{\mathcal E_N(pt,z)}{\mathcal E_N(t,z)}
       =\frac{a(t,z)}{\operatorname{Norm}(a)(t,z)^{1/N}},
 \tag{5d}
\]
with the anchored norm root. On \(\mathcal H_N\) it is a normalized
solution, so (5b) applies. Off shell, (5) implies that its logarithmic
coefficients through degree \(N-1\) still equal those of \(G_N\).
Hence \(\mathcal E_N-G_N\in(t^N)\), coefficientwise in \(z\), on
its Taylor domain. Its branch divisors are the explicitly displayed
zeros and poles of the finitely many \(a(p^kt,z)\).

## 2. Exact factorization at every physical node

Write \(a_l(t)=1+q^{-1}Q^lt\), with integer \(l\). Then
\(D_N(t)=\prod_{l=1}^N a_l(t)\).

**Proposition 1.** For every \(0\le j\le d\),
\[
 \boxed{\quad
 G_N(t;c_j)=D_N(t)
       \frac{\prod_{l=-j+1}^{0}a_l(t)}
            {\prod_{l=1}^{j+1}a_l(t)} .
 \quad}
 \tag{6}
\]
The displayed quotient has its removable values at the canceled
factors. It is an ordinary polynomial of degree \(d\), with constant
coefficient one. All its zeros lie on
\[
                         t^N=\eta .
 \tag{7}
\]

**Proof.** The denominator in (6) consists of distinct factors of
\(D_N\), so cancellation gives a polynomial of degree
\(N-(j+1)+j=d\). Its constant coefficient is one. Since
\(a_l(pt)=a_{l-1}(t)\), its shift ratio is
\[
 \frac{a_{-j}(t)a_{j+1}(t)}{a_0(t)^2}
        =\frac{1+c_jt+t^2}{(1+q^{-1}t)^2}.
 \tag{8}
\]
Thus it satisfies (3) at \(z=c_j\). In degrees \(1,\ldots,d\),
the coefficient recursion has nonzero factors \(p^a-1\).
The constant coefficient therefore determines the degree-\(d\)
solution uniquely. This proves (6).
Every remaining numerator factor is one of the factors of \(D_N\),
possibly repeated, proving (7). \(\square\)

It follows that \(G_N(t)\) is a unit of the complete algebra
\(\mathcal H_N\) for \(D_N(t)\ne0\): its value at every spectral
root is nonzero. This statement uses the ordinary unit criterion
in each local factor \(\mathbb C[\epsilon]/\epsilon^m\);
it does not discard its nilpotent coordinate.

## 3. A uniform phase and amplitude on the physical unit disk

For \(|t|<1\) and \(z\) in a neighborhood of \([-2,2]\), define
the analytic branches
\[
 A(t,z)=b(t,z)^{-1/2},\qquad
 \Phi(t,z)=-\frac1{2\pi i}\int_0^t
       \frac{\log b(u,z)-2\log(1+u)}u\,du .
 \tag{9}
\]
They are normalized by \(A(0,z)=1,\Phi(0,z)=0\).
For any fixed closed subdisk, a common complex neighborhood of
\([-2,2]\) suffices. The integrand at zero is removable.
At \(z=w+w^{-1}\), this is equivalently
\[
 \Phi(t,z)=\frac{
       \operatorname{Li}_2(-wt)+\operatorname{Li}_2(-w^{-1}t)
                       -2\operatorname{Li}_2(-t)}{2\pi i},
 \tag{10}
\]
where the analytic branches in (9), not a new cut, determine (10).

**Proposition 2.** For every \(0<\rho<1\), uniformly for all
physical indices and levels,
\[
 G_N(t;c_j)=D_N(t)A(t,c_j)e^{N\Phi(t,c_j)}
                            (1+O_\rho(N^{-1})),
                    \qquad |t|\le\rho .
 \tag{11}
\]
The relative error is holomorphic in \(t\), and its fixed
\(t\)-derivatives are \(O(N^{-1})\) on smaller disks.

**Proof.** Put \(u_j=(j+1/2)/N\), and set
\(F(v)=\log(1+te^{2\pi iv})\), using its branch at \(t=0\).
All its required real-\(v\) derivatives are uniformly bounded for
\(|t|\le\rho<1\). The numerator product in (6) samples midpoints
on \([-j/N,0]\); the denominator samples midpoints on
\([0,(j+1)/N]\). Composite midpoint summation, followed by moving
the two outer endpoints by \(1/(2N)\), gives
\[
 \log\frac{G_N(t;c_j)}{D_N(t)}
  =N\!\left(\int_{-u_j}^0F(v)\,dv-\int_0^{u_j}F(v)\,dv\right)
             -\frac{F(-u_j)+F(u_j)}2+O_\rho(N^{-1}).
 \tag{12}
\]
The midpoint error is bounded by a constant times
\((j+1)/N^2\le1/N\). The endpoint Taylor errors are also \(O(1/N)\).
This includes \(j=0,d\); no interior-index restriction is used.
The integral in (12) is \(\Phi(t,c_j)\), and the two endpoint
terms give \(\log A(t,c_j)\). Exponentiation proves (11).
Cauchy's formula on nested disks gives the derivative statement.
\(\square\)

## 4. The actual first normal and its central correction

The value formula alone cannot be differentiated in the discrete
index \(j\). Instead differentiate the actual polynomial \(G_N(t;z)\)
in its Casimir variable \(z\).

Fix a double node \(c_j=2\cos\theta_j\), where
\(\theta_j=(2j+1)\pi/N\); thus \(\sin\theta_j\ne0\).
Set
\[
 H_j(t)=\frac{\partial_zG_N(t;c_j)}{G_N(t;c_j)},\qquad
 R_j(t)=\frac{t}{b(t,c_j)}.
 \tag{13}
\]
These are rational functions. Differentiating (3), and using
\(P_N'(c_j)=0\), gives
\[
                         H_j(pt)-H_j(t)=R_j(t).
 \tag{14}
\]
The differentiated cyclic norm identity (5) gives
\(\sum_{k=0}^{d}R_j(p^kt)=0\).

**Proposition 3.** The actual logarithmic derivative is
\[
 \boxed{\quad
 H_j(t)=\frac1N\sum_{k=0}^{d}kR_j(p^kt)
       -\eta\,\frac{d-2j}{2i\sin\theta_j}\,
                                      \frac{t^N}{D_N(t)} .
 \quad}
 \tag{15}
\]
In particular the central function of \(t^N\) is retained.

**Proof.** Let \(H_{\rm part}=N^{-1}\sum kR_j(p^kt)\).
Reindexing this finite sum and using its zero cyclic average proves
(14) for \(H_{\rm part}\). Thus \(H_j-H_{\rm part}\) is invariant
under \(t\mapsto pt\).

All its poles lie on (7). It vanishes at zero and is bounded at
infinity: \(G_N(t;c_j)\) has degree exactly \(d\), while its
Casimir derivative has degree at most \(d\). At
\(t_*=-q^{-1}\), formula (6) shows \(G_N(t_*;c_j)\ne0\),
because the factor \(a_1\) is canceled and is not restored by
the numerator. Hence the invariant difference has at most a
simple pole there. Cyclic invariance implies the same at every
point of (7). Multiplication by \(D_N\) now gives an invariant
polynomial of degree at most \(N\), vanishing at zero.
Consequently the difference is \(C t^N/D_N\).

Write \(w=e^{i\theta_j}=qQ^j\). At \(t_*\), only terms
\(k=j,d-j\) in \(H_{\rm part}\) can have a pole. Their
residues in \(R_j(p^kt)\) are, respectively,
\(-q^{-1}/(w-w^{-1})\) and \(q^{-1}/(w-w^{-1})\).
Therefore
\[
 \operatorname{Res}_{t=t_*}H_{\rm part}
       =\frac{q^{-1}(d-2j)}{N(w-w^{-1})},\qquad
 \operatorname{Res}_{t=t_*}\frac{t^N}{D_N(t)}
       =\frac{\eta q^{-1}}N .
 \tag{16}
\]
Canceling this pole fixes
\(C=-\eta(d-2j)/(w-w^{-1})\), proving (15). \(\square\)

There is a useful equivalent finite sum. Choose the representative
\(0\le j<d/2\) of a double node and set
\[
 s_j=2i\sin\theta_j,\qquad
 F_l(t)=\frac{q^{-1}Q^lt}{1+q^{-1}Q^lt}.
\]
Then
\[
                 H_j(t)=\frac1{s_j}
                               \sum_{l=j+2}^{N-j}F_l(t).
 \tag{16a}
\]
Indeed \(R_j=(F_{j+1}-F_{-j})/s_j\). Cyclic reindexing of
the weighted sum in (15) gives
\[
 H_{\rm part}=\frac1{s_j}\left[
       \sum_{l=j+2}^{N-j}F_l-\frac{d-2j}{N}
                                      \sum_{l=1}^NF_l\right].
\]
Since \(\sum_{l=1}^NF_l=tD_N'/D_N=-\eta Nt^N/D_N\), its
last term cancels the central correction exactly. This is a
cancellation proved with the central term present, not permission
to omit that term in the primitive.

**Theorem 4.** Define the actual relative error near the physical
nodes by
\[
 \epsilon_N(t,z)=
       \frac{G_N(t;z)}{D_N(t)A(t,z)e^{N\Phi(t,z)}}-1 .
 \tag{17}
\]
For every \(\rho<1\), its complete physical Hermite data obey
\[
 |\epsilon_N(t,c_j)|\le C_\rho/N,\qquad
 |\partial_z\epsilon_N(t,c_j)|\le C_\rho/N
                       \quad(c_j\ \hbox{double}),\qquad |t|\le\rho .
 \tag{18}
\]
Only the value is required at the odd simple node \(-2\).
Fixed \(t\)-derivatives have the same bounds on smaller disks.

**Proof.** The value estimate is Proposition 2. To estimate (15),
expand
\[
 R_j(t)=\sum_{n\ge1}r_nt^n,\qquad
 r_n=(-1)^{n-1}\frac{\sin(n\theta_j)}{\sin\theta_j}.
 \tag{19}
\]
For all real physical nodes, \(|r_n|\le n\). At double nodes
\(r_{\ell N}=0\). Finite Fourier summation in \(H_{\rm part}\)
therefore gives coefficient \(r_n/(p^n-1)\) when \(N\nmid n\)
and zero otherwise.

For \(n\le N/2\), the Bernoulli expansion, uniformly away from
its next pole, gives
\[
 \frac{r_n}{p^n-1}
        =-\frac{r_n}{(2\pi i/N)n}-\frac{r_n}2
                                      +O(n^2/N).
 \tag{20}
\]
Every Taylor coefficient of the actual \(H_j\) has bound \(CN^2\):
formula (16a) has at most \(N\) summands with coefficient modulus
one, and \(|\sin\theta_j|\ge2/N\). Thus its tail above \(N/2\)
costs at most a polynomial in \(N\) times \(\rho^{N/2}\).
The leading terms in (20) have the same tail bound, since
\(|r_n|\le n\). The central term starts at degree \(N\) and
has coefficient bounded by \(CN^2\), consistent with this estimate.
Summing (20) and these tails proves
\[
 H_j(t)=N\Phi_z(t,c_j)
           -\frac{t}{2b(t,c_j)}+O_\rho(N^{-1}).
 \tag{22}
\]
Here
\(\Phi_z=-(2\pi i)^{-1}\int_0^tdu/b(u,z)\), directly from (9),
and \(A_z/A=-t/(2b)\).
Taking the logarithmic derivative of (17) at the actual double
node now proves the second estimate in (18). No value-only
interpolation was differentiated. Holomorphy in \(t\) and
Cauchy estimates prove the remaining assertions. \(\square\)

The theorem is a relative estimate in the full physical Hermite
coordinates. It is not a uniform estimate in the Newton packet norm,
whose conversion can amplify componentwise errors.

## 5. Original source normalizations

The functional \(\psi(g)=\phi((R^+)^2g)/N\) satisfies
\(\psi(p_ap_b)=\delta_{ab}\). Hence, exactly,
\[
                              \psi(G_N(t))=1.
 \tag{23}
\]
This is the fixed source normalization of the section, not an
unknown knot value. With \(x=-q^{-1}\), define the actual open packet
\[
             \mathcal F_N(t)=\frac{R^+G_N(t)}{\sqrt N}
                                  =\sum_{a=0}^{d}f_at^a .
\]
The two original closure rows of the centered compiler give
\[
 \boxed{\quad
 \phi(\mathcal F_N(t))
       =\frac{\kappa^{-1}D_N(t)}{\sqrt N(1-xt)},\qquad
 m(\mathcal F_N(t))
       =\frac{\kappa D_N(t)}{\sqrt N(1-x^{-1}t)}.
 \quad}
 \tag{24}
\]
Both formulas have their removable polynomial values at a canceled
factor. In particular neither closing vanishes off (7). Their
scalar rate on fixed interior disks is zero; no hyperbolic volume
has been assigned to these normalizing packets.

## 6. An exponentially accurate section and its off-spectrum germ

The exact low-degree logarithm supplies a zero-free analytic section.
Let \(S_n(z)=2T_n(z/2)\), and set
\[
 \ell_{N,n}(z)=
  \frac{(-1)^{n+1}(S_n(z)-2q^{-n})}{n(p^n-1)}
                 \quad(1\le n<N),\qquad
 U_N(t,z)=\exp\!\left(\sum_{n=1}^{N-1}\ell_{N,n}(z)t^n\right).
 \tag{25}
\]
The forcing in (3) starts at degree \(N\), so the formal logarithm
of \(G_N\) through degree \(N-1\) is exactly the exponent in (25).
Thus \(G_N-U_N\) is divisible by \(t^N\), coefficientwise as a
formal series of ordinary polynomials in \(z\).

On the full physical Hermite coordinates one has the stronger estimate
\[
 \boxed{\quad
 \left|\frac{G_N(t;c_j)}{U_N(t,c_j)}-1\right|
 +\left|\left.\partial_z\!
             \left(\frac{G_N(t;z)}{U_N(t,z)}\right)\right|_{z=c_j}\right|
          \le C_\rho N^2\rho^N,\qquad |t|\le\rho<1 ,
 \quad}
 \tag{25a}
\]
where the derivative is required only at double nodes. For a simple
node only the first summand occurs.

To prove this, use the logarithm of \(G_N(t;c_j)\) equal to zero
at \(t=0\). Proposition 1 puts every zero on the unit circle and
there are exactly \(d\) zeros with multiplicity. Its degree-\(n\)
logarithmic coefficient therefore has magnitude at most \(d/n\).
After the first \(N-1\) matching coefficients, its tail on the
disk has bound \(C_\rho\rho^N\). At a double node, (16a)
bounds every Taylor coefficient of \(G_z/G\) by \(CN^2\).
Its first \(N-1\) coefficients also agree with \(\partial_z\log U_N\);
the remaining tail is at most \(C_\rho N^2\rho^N\).
Exponentiation and logarithmic differentiation prove (25a).
Fixed \(t\)-derivatives remain exponentially small on smaller disks.

There is also a safe common germ at arbitrary fixed Casimir labels.
It is useful to state its size limitation explicitly.
For every fixed compact set \(\Lambda\) of Casimir labels and every
prescribed \(c>0\), there is \(r>0\) such that
\[
 G_N(t;z)=U_N(t,z)(1+O(e^{-cN})),
                         \qquad z\in\Lambda,\quad |t|\le r.
 \tag{26}
\]
One may enlarge \(\Lambda\) before choosing \(r\); fixed derivatives
then have the same exponential bound on smaller compact sets.
In particular this is a nonzero section for sufficiently large \(N\),
including off-spectrum \(z\).

Here are quantitative reasons for (26). On an enlarged compact
\(\Lambda\), the monic recurrence bounds
\(|\mathcal P_a(z)|\le C^a\). The elementary sine-product bound
\[
 e^{-C_0N}\le |(p;p)_a|\le e^{C_0N}\quad(0\le a<N)
 \tag{27}
\]
then gives \(|p_a(z)|\le e^{C_1N}\).
For the lower bound in (27), use
\(2\sin(\pi k/N)\ge4\min(k,N-k)/N\), discard factors at least
one, and compare the remaining sum of logarithms with
\(\int_1^m\log u\,du\). Its total negative part is \(O(N)\).

Also \(|S_n(z)|\le C_2^n\) on that compact. On a sufficiently small
fixed circle \(|t|=R\), (25) has
\(|\log U_N|\le C_3N\): split \(n\le N/2\), where
\(|p^n-1|\ge c_0n/N\), from its complementary range, where
\(|p^n-1|\ge c_0(N-n)/N\).
Consequently \(G_N-U_N\) has supremum at most \(e^{C_4N}\)
on that circle. Its zero of order at least \(N\) gives
\[
 |G_N-U_N|\le e^{C_4N}(|t|/R)^N
                     \quad(|t|<R).
 \tag{28}
\]
On a smaller fixed disk \(|U_N^{-1}|\le e^{C_5N}\).
Choose \(r/R\) so small that (28) after this multiplication is
at most \(e^{-cN}\). This proves (26), with Cauchy estimates
on nested parameter domains proving the derivative statement.

For clarity, the coefficient expansion on \(n\le N/2\) is
\[
 \ell_{N,n}(z)=(-1)^n\left[
       \frac{N(S_n(z)-2)}{2\pi i n^2}+\frac{S_n(z)}{2n}\right]
                                +O(C_\Lambda^n/N).
 \tag{28a}
\]
It follows by expanding \((e^{-2\pi in/N}-1)^{-1}\) and
\(q^{-n}=e^{-\pi in/N}\) on \(|2\pi n/N|\le\pi\).
On \(C_\Lambda|t|<1/2\) the error sums to \(O(N^{-1})\).
The complementary coefficients, bounded as above, have exponentially
small sums there. The two displayed main series are \(N\Phi\)
and \(\log A\), respectively. Thus
\[
 U_N(t,z)=A(t,z)e^{N\Phi(t,z)}(1+O(N^{-1})).
 \tag{29}
\]
The leading phase and nonzero amplitude are therefore those in
(9). Keeping the full explicit exponent (25), rather than just
(29), supplies the exponential accuracy. A fixed geometric Casimir
label can be included in \(\Lambda\); no assertion places its
required geometric generating coordinate inside the disk in (26).

## 7. Exact assembly with nonnegative powers

The local ambiguity (5b) is harmless in one specified full source
construction. It is not a rule for deleting an arbitrary intermediate
boundary component.

Take a finite original Conway compiler tree in the centered basis.
Compress genuine turns into edge parities, so the gluing on each
internal edge is either \(\delta_{ab}\) or
\(\delta_{a+b,d}\). Keep each signed input, unit and final marked
closing as its own vertex, with all recorded scalars.
On a tree, choose vertex reversals recursively so that every edge
becomes anti-diagonal: if its original parity is \(e_{vw}\), set
\[
                   s_w=1+e_{vw}+s_v\pmod2
 \tag{30}
\]
after choosing one root reversal. Simultaneously reversing every
incident index turns a trivalent tensor \(C\) into \(\bar C\).
At one-valent inputs and closing vertices it explicitly reverses
the given finite vector. Thus all arrays and source rows remain known.

For a vertex \(v\), form its finite generating polynomial
\[
 V_v((t_e)_{e\ni v})
     =\sum_{0\le a_e\le d} T_v((a_e)_{e\ni v})
                                      \prod_{e\ni v}t_e^{a_e}.
 \tag{31}
\]
The original scalar is exactly
\[
              \boxed{\quad
              [\,\prod_e t_e^d\,]\prod_v V_v .
              \quad}
 \tag{32}
\]
Indeed each edge receives two nonnegative powers, and the selected
coefficient enforces their sum to be \(d\), precisely its
anti-diagonal contraction.

It follows that any vertex may be replaced by a nonnegative-power
formal series agreeing with it modulo the ideal generated by the
incident \(t_e^N\). Expand the difference of the two full products
by changing one vertex at a time. Every term then has exponent at
least \(N>d\) in one edge variable; the other factors have no
negative powers, so it cannot contribute to (32).

In particular the exact trivalent polynomial is
\[
 V_C(t_1,t_2,t_3)
   =N^{-1/2}\psi\!\left(
        R^+G_N(t_1;z)G_N(t_2;z)G_N(t_3;z)\right).
 \tag{33}
\]
This is the original \(C\), not an ordinary untwisted polynomial
linearization. Replacing its leg sections by \(U_N\) from (25)
preserves all coefficients through degree \(d\) in each variable,
and hence the complete source (32), exactly. The analytic cochain
\(\mathcal E_N\) in (5c) is another eligible leg replacement.
This uses equality of
the coefficients as full algebra elements, not merely their values
at distinct spectral roots. The same assertion applies to the
corresponding coefficient-conjugate sections at a \(\bar C\) vertex.

More generally the factors in (5b) change no such assembled source:
their difference from one starts in degree \(N\) in that leg.
Their coefficients may lie in the full algebra; applying the
specified \(\psi\) or \(\phi\) does not reduce the leg degree.
Thus this central ambiguity acts trivially on this full coefficient
functional.

The order matters. First reverse the finite tensors, then choose
nonnegative-power extensions of the resulting arrays. Applying
\(t^dG(1/t)\) to an already untruncated section introduces negative
powers and invalidates the ideal argument. Nor is (32) a statement
about arbitrary factors in a meridian or a quantum normal parameter.
For analytic sections it has the original small Taylor-circle cycle.
A later deformation toward a geometric saddle must still track
every pole, branch and contributing cycle.
Sectorial terms such as \(t_e^N\log t_e\) are not Taylor sections
and are not covered. Nor is a factor in \((t_e/t_f)^N\) covered
unless its complete expansion has nonnegative powers in every
edge variable.

## 8. Scope and complete proof source

The exact forced equation, norm identity, physical factorization,
and source rows concern the original full finite algebra.
The first-normal estimate retains its nilpotent directions.
The parameter \(t\) here generates the centered label; it is not
the moving cap-resolvent coordinate or a peripheral meridian.

These statements do not provide an asymptotic for the triple
generating period
\(\psi(R^+G_N(t_1)G_N(t_2)G_N(t_3))\), nor prove a nonzero
coefficient after arbitrary signed short-component assembly.
The uniform physical Hermite estimate and the small off-spectrum
germ must not be promoted to an uncontrolled larger spectral chart,
Newton-norm approximation, or source-normal volume certificate.

The sole complete proof direct was read at its matching pin:

| Source | SHA-256 |
|---|---|
| [Centered source compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

The complete [Jacobi generating-unit note](research_actual_jacobi_generating_unit.md),
[physical-angle crossing transport](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_current_free_aw_crossing_transport.md),
the [arbitrary-power source compiler](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_arbitrary_power_source_compilation.md),
and [finite Fourier-band theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_newton_interpolation_finite_fourier_band.md)
were read for coverage. They already supply local analytic units,
source-aware difference transport and exact finite Fourier
representations. Their estimates are not imported here. The Jacobi
unit theorem excludes its full-degree endpoint; the estimates above
use the actual full-\(N\) polynomial and prove its complete first
normal on the entire physical unit disk.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical iteration, test, build, git operation
or earlier-final edit was performed.
