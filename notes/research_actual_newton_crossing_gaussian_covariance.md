# Gaussian and endpoint kernels for the actual Newton crossing

20 November 2026. The full original crossing has a positive Hermitian
row covariance, even though its phases cannot all be removed by a
diagonal change of coordinates. This note calculates that covariance
in two regimes. In the interior of the Newton index interval its
normalized kernel is Gaussian at scale \(\sqrt N\). At either endpoint,
any fixed number of rows has the same explicit Pascal moment kernel
after the stated polynomial row rescaling. These are asymptotics of the
actual finite crossing, with its Cartan scalar and both closing indices
retained.

The results do not give a norm estimate for an arbitrary short tangle.
They do not identify a reflected norm with the original scalar closure,
or show that its geometric contribution survives arbitrary gluing.

## 1. The exact covariance and its phases

Put \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\[
 s_0=1,\qquad s_a=\prod_{u=1}^a2\sin(\pi u/N),\qquad
 \beta_{ik}=\frac{s_i}{s_ks_{i-k}}\quad(0\leq k\leq i\leq d).
                                                               \tag{1}
\]
Set \(\beta_{ik}=0\) outside this triangular support. The actual
Newton crossing of
[the source-exact crossing theorem](actual_newton_twist_canonical_graph.md),
Section 1, is
\[
 T_{ik}=\kappa(-1)^iq^{i+k^2}{i\brack k}_Q,
 \qquad \kappa=q^{d^2/2}.                              \tag{2}
\]
All fractional powers of \(q\) in this note mean their displayed
exponentials. The finite root factorial phase gives
\[
 {i\brack k}_Q=q^{k(i-k)}\beta_{ik},\qquad
 T_{ik}=\kappa D_iq^{ik}\beta_{ik},\qquad
 D_i=(-1)^iq^i.                                       \tag{3}
\]
Thus no quadratic phase in \(k\) has been omitted from (2); it has
combined with the actual factorial phase in (3).

Write \(D=\operatorname{diag}(D_i)\). Define the covariance and a
fixed diagonal unitary matrix by
\[
 \mathcal C=TT^*,\qquad
 U_i=D_iq^{i^2/4},\qquad K=U^*\mathcal C U.
\]
Here and below \(U_i\) denotes the \(i\)-th diagonal entry of \(U\).
The exact kernel is
\[
 K_{ij}=q^{-(i^2-j^2)/4}
     \sum_{k=0}^{\min(i,j)}\beta_{ik}\beta_{jk}q^{(i-j)k}.
                                                               \tag{4}
\]
The scalar \(\kappa\) cancels in this covariance because
\(|\kappa|=1\); it remains in the actual rows \(T\). The unitary
matrix \(U\) is explicit and independent of any tangle value. Formula
(4) does not assert that \(K\) is entrywise real at finite \(N\).

Both original closures remain those of the complete Newton algebra:
the cup-mark closure is coefficient row \(e_0^*\), and the cylindrical
closure with its original ordinary trace and mark is row \(e_d^*\).
The exact physical-source intertwiner and all external framing factors
are those of the cited crossing theorem, Section 4. In particular,
\(i=0,d\) below refer to these same Newton boundary indices.

## 2. The uniform interior theorem

Let
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 B(x)=J(x)-2J(x/2),\qquad
 c(x)=\pi\cot(\pi x/2).
\]
For a compact interval \(I\subset(0,1)\), the row energies satisfy,
uniformly for \(x=i/N\in I\),
\[
 \boxed{\quad
 \mathcal C_{ii}
 =\sqrt{\frac{c(x)}{2\pi N}}\,
       e^{2NB(x)}(1+o(1)).
 \quad}                                                   \tag{5}
\]
For each fixed \(H<\infty\), put
\[
 a=\frac{i+j}{2N},\qquad h=\frac{i-j}{\sqrt N}.
\]
Then, uniformly over \(a\in I\), \(|h|\leq H\),
\[
 \boxed{\quad
 \frac{K_{ij}}{\sqrt{\mathcal C_{ii}\mathcal C_{jj}}}
 =\exp\!\left[-\frac{\pi h^2}{4\sin(\pi a)}\right]+o(1).
 \quad}                                                   \tag{6}
\]
Uniformity includes arbitrary integer choices of \(i,j\) in this
range. No parity subsequence or rounding convention is required.

### 2.1 Factorial estimates with their prefactors

For every compact subinterval of \((0,1)\), uniformly for
\(x=n/N\) in that subinterval,
\[
 s_n=\sqrt{2N\sin\pi x}\,e^{NJ(x)}(1+O(N^{-1})).       \tag{7}
\]
To prove (7), write
\(h_0(t)=\log(\sin\pi t/(\pi t))\). It extends smoothly at zero
and has bounded derivatives on \([0,1-\delta]\). Stirling's formula
and the trapezoidal sum estimate give
\[
\begin{split}
 \log s_n
 &=n\log(2\pi/N)+\log(n!)+\sum_{u=1}^nh_0(u/N)\\
 &=NJ(x)+\tfrac12\log(2\pi Nx)+\tfrac12h_0(x)+O(N^{-1})\\
 &=NJ(x)+\tfrac12\log(2N\sin\pi x)+O(N^{-1}).
\end{split}
\]
The errors are uniform because \(n\) is a fixed positive fraction
of \(N\).

We will also use the weaker endpoint-uniform estimate
\[
 \log s_n=NJ(n/N)+O(\log N),\qquad 0\leq n<N.          \tag{8}
\]
Subtracting \(\log t+\log(1-t)\) from
\(\log(2\sin\pi t)\) leaves a continuously differentiable function
on \([0,1]\). Its Riemann-sum error is bounded uniformly in the
upper endpoint. Integral comparison for the two logarithms gives
the \(O(\log N)\) error. This proves (8), including \(n=0,N-1\).

Put
\[
 b(x,z)=J(x)-J(z)-J(x-z),\qquad 0\leq z\leq x<1.
\]
Where \(x,z,x-z\) stay in fixed interior intervals, (7) implies
\[
 \beta_{ik}
 =\frac1{\sqrt{2N}}
    \sqrt{\frac{\sin\pi x}{\sin\pi z\sin\pi(x-z)}}
    e^{Nb(x,z)}(1+O(N^{-1})),
 \quad x=i/N,\ z=k/N.                                \tag{9}
\]
Its maximum in \(z\) is at \(x/2\), because it is symmetric and
\[
 b_{zz}(x,z)
 =-\pi\frac{\sin\pi x}{\sin\pi z\sin\pi(x-z)}<0.
                                                               \tag{10}
\]
For \(x\in I\), the negative quadratic bound from (10) can be
chosen uniformly on the whole open interval \(0<z<x\). Estimate
(8) then controls the same tails with at most a polynomial factor.

### 2.2 The row energy

Set \(x=i/N\) and \(t=(k-Nx/2)/\sqrt N\). On each fixed
bounded \(t\)-interval, (9) and Taylor expansion give
\[
 \beta_{ik}^2
 =\frac{c(x)}{\pi N}e^{2NB(x)}
            e^{-2c(x)t^2}(1+o(1)),                  \tag{11}
\]
uniformly for \(x\in I\). The lattice spacing in \(t\) is
\(N^{-1/2}\). Hence summing (11) gives (5), since
\(\int_{\mathbb R}e^{-2ct^2}dt=\sqrt{\pi/(2c)}\).

Here is a common tail justification for this step and the next.
Choose \(0<\varepsilon<1/6\). On
\(|t|\leq N^\varepsilon\), third derivatives on a fixed interior
neighborhood bound the exponent remainder by
\(O(N^{-1/2+3\varepsilon})=o(1)\); (9)'s prefactors are uniformly
smooth there. Outside this range, (10) and (8) bound the normalized
sum by a polynomial times \(e^{-c_0N^{2\varepsilon}}\), uniformly
in \(x\in I\), for some \(c_0>0\). In the interior range, a
uniform Gaussian bound gives the usual Riemann-sum convergence.
This proves the displayed estimates uniformly, rather than only at
one selected central lattice point.
For the mixed sum, apply the same quadratic bound separately at
\(x=i/N\) and \(x=j/N\). Their maximizing indices differ by
\(O(\sqrt N)\); the sum of the two quadratic bounds is centered at
\((i+j)/4\). This gives the same tail estimate about that center.

### 2.3 The mixed kernel

Write \(i/N=a+\epsilon\), \(j/N=a-\epsilon\), where
\(\epsilon=h/(2\sqrt N)\), and set
\(t=(k-Na/2)/\sqrt N\). Let \(c=c(a)\). The sum of the two
real exponents in (9) is
\[
\begin{split}
 N\{b(a+\epsilon,k/N)+b(a-\epsilon,k/N)\}
 =2NB(a)+\frac{h^2}{4}\{J''(a)-c\}-2ct^2+o(1).
\end{split}                                                   \tag{12}
\]
Indeed \(b_z(a,a/2)=0\), \(b_{zz}(a,a/2)=-2c\), and
\(b_{xx}(a,a/2)=J''(a)-c\). The mixed \(\epsilon t\) terms
cancel between the two copies. The prefactor product in (9) is
\(c/(\pi N)(1+o(1))\) in this range.

The phase in (4) is exactly
\[
 q^{(i-j)k}=q^{(i^2-j^2)/4}e^{i\pi ht}.               \tag{13}
\]
The chirp already included in \(K\) removes the first factor.
Using the uniform tail argument above, the remaining mixed sum is
therefore its real Gaussian integral with Fourier multiplier
\(e^{i\pi ht}\). Its ratio to the zero-frequency integral is
\[
 \frac{\int e^{-2ct^2+i\pi ht}dt}
      {\int e^{-2ct^2}dt}
        =e^{-\pi^2h^2/(8c)}.                         \tag{14}
\]
Finally
\(B''(a)=J''(a)-c/2\). Comparing (12) with the two diagonal
exponents in (5) contributes the further factor \(e^{-ch^2/8}\).
Since
\[
 c+\pi^2/c=\frac{2\pi}{\sin\pi a},
\]
their product is (6). This completes the uniform proof of the
interior theorem.

## 3. Both endpoint limits

Fix a nonnegative integer \(R\). In this section \(0\leq r,s\leq R\)
are fixed while \(N\) tends to infinity. They count Newton rows from
an endpoint; they are not reinterpreted as Casimir derivative orders.
Define the positive matrix
\[
 A_{rs}=\binom{r+s}{r}\qquad(0\leq r,s\leq R).          \tag{15}
\]
At the lower endpoint,
\[
 K_{rs}\longrightarrow A_{rs}.                         \tag{16}
\]
At the upper endpoint put
\[
 W_{N,r}=\sqrt N\,\frac{(N/(2\pi))^r}{r!}.
\]
Then
\[
 \boxed{\quad
 \frac{K_{d-r,d-s}}{W_{N,r}W_{N,s}}
       \longrightarrow A_{rs}.
 \quad}                                                   \tag{17}
\]
The convergence is simultaneous on each fixed finite block.
Consequently either endpoint has normalized correlation limit
\[
 \frac{A_{rs}}{\sqrt{A_{rr}A_{ss}}}
 =\frac{(r+s)!}{\sqrt{(2r)!(2s)!}}.                    \tag{18}
\]

For (16), fixed factorial indices in (1) give
\(\beta_{rk}\to\binom rk\). All phase factors in (4) tend to one,
so its limit is
\(\sum_k\binom rk\binom sk=\binom{r+s}{r}\), by Vandermonde.

For (17), the exact reflection identity \(s_as_{d-a}=N\) gives
\[
 \beta_{d-r,k}=\frac{s_{k+r}}{s_rs_k}
 =\frac{\prod_{u=1}^r2\sin(\pi(k+u)/N)}{s_r},
 \qquad 0\leq k\leq d-r.                              \tag{19}
\]
Since \(s_r=(2\pi/N)^rr!(1+O_R(N^{-2}))\), zero extension
past this support gives the uniform limit
\[
 N^{-r}\beta_{d-r,k}
 =\frac{\sin^r(\pi k/N)}{\pi^rr!}+O_R(N^{-1})
       \qquad(0\leq k<N).                            \tag{20}
\]
For \(r>0\), the omitted last \(r\) terms obey the same error
bound because their \(\sin^r(\pi k/N)=O_R(N^{-r})\).
For \(r=0\), the formula is exact and all indices occur.

Before the chirp in (4), the scaled covariance is thus a Riemann sum:
\[
\begin{split}
 &N^{-(r+s+1)}(D^*\mathcal CD)_{d-r,d-s}\\
 &\hspace{8mm}\longrightarrow
 \frac1{\pi^{r+s}r!s!}
       \int_0^1\sin^{r+s}(\pi t)e^{i\pi(s-r)t}\,dt.
\end{split}                                                   \tag{21}
\]
Expanding the sine power into exponentials gives exactly
\[
 \int_0^1\sin^{r+s}(\pi t)e^{i\pi(s-r)t}dt
 =\mathrm i^{s-r}2^{-(r+s)}\binom{r+s}{r}.             \tag{22}
\]
Indeed every exponential has integer even frequency on \([0,\pi]\);
only its constant term survives. Here \(\mathrm i\) is the imaginary
unit. The chirp factor in (4), at
\(i=d-r,j=d-s\), tends to \(\mathrm i^{r-s}\). Equations (21)--(22)
therefore give (17), with its precise positive row factors.

In particular
\[
 \mathcal C_{d-r,d-r}
 \sim\frac{N^{2r+1}}{(2\pi)^{2r}(r!)^2}\binom{2r}{r}.
                                                               \tag{23}
\]
The case \(r=0\) is the exact identity
\(\mathcal C_{dd}=N\); the original last closing row is included.

## 4. An explicit orthogonal frame on each fixed endpoint block

Let \(P\) be the \((R+1)\)-dimensional lower triangular Pascal
matrix,
\[
 P_{rk}=\binom rk\ (k\leq r),\qquad
 (P^{-1})_{rk}=(-1)^{r-k}\binom rk.
\]
Vandermonde gives the exact factorization
\[
 A=PP^{\mathsf T}.                                    \tag{24}
\]
Alternatively, (18) is the Gram of the normalized monomials
\(t^r/\sqrt{(2r)!}\) in \(L^2(\mathbb R_+,e^{-t}dt)\).
Both descriptions prove strict positive definiteness of every fixed
block.

Take the actual row vectors of \(U^*T\). On its lower endpoint
block, apply \(P^{-1}\). On its upper endpoint block, in the order
\(d,d-1,\ldots,d-R\), first divide row \(r\) by \(W_{N,r}\),
then apply \(P^{-1}\). Equations (16)--(17) and (24) say that the
resulting row Grams converge to the identity. Their condition numbers
are therefore uniformly bounded for all sufficiently large \(N\),
with \(R\) fixed. The only \(N\)-dependent magnitudes in this
orthogonalization are the displayed polynomial factors \(W_{N,r}\).

The two endpoint blocks can also be used together. For fixed
\(r,s\leq R\), the sum for the mixed entry has only \(k\leq r\).
Formula (19) at fixed \(k\) gives
\(\beta_{d-s,k}\to\binom{s+k}{s}\), while
\(q^{(r-d+s)k}\to(-1)^k\). Consequently
\[
 (D^*\mathcal CD)_{r,d-s}
 \longrightarrow\sum_{k=0}^r(-1)^k\binom rk\binom{s+k}{s}
 =(-1)^r\binom sr.                                    \tag{25}
\]
The last binomial is zero when \(r>s\). One proof extracts the
coefficient of \(z^s\) from
\((1+z)^s[1-(1+z)]^r=(-1)^rz^r(1+z)^s\).
The extra chirp has modulus one, so the corresponding mixed
\(K\)-entries are \(O_R(1)\). Dividing the upper rows by
\(W_{N,s}\) makes the whole mixed block tend to zero.

For \(N>2R+1\), the lower and upper row sets are disjoint.
Stack their two explicitly rescaled and Pascal-transformed row
families. Its full Gram, including the mixed block, therefore obeys
\[
 \operatorname{Gram}(\text{combined endpoint rows})
       \longrightarrow I_{2R+2}.                     \tag{26}
\]
This is simultaneous asymptotic orthogonality of the two finite
boundary windows, with their actual mixed phases retained.

The first row of \(P^{-1}\) is \(e_0^*\). Thus the original
endpoint row is kept: at the upper endpoint it is exactly
\(\overline{U_d}\,e_d^*T/\sqrt N\), and at the lower endpoint it
is \(e_0^*T\). These known phases and powers of \(N\) are retained
when pairing with an actual source. No unknown period defines the
frame or its normalization.

This is a fixed-\(R\) result. It supplies no uniform conditioning
when \(R\) grows proportionally to \(N\), and no completeness
claim for a truncated endpoint packet. The whole crossing still
contains every repeated-root channel of the original algebra.

## 5. Geometric meaning and the remaining gluing step

The positive row amplitude in (1) is already an exact angle weight:
\[
 \beta_{ik}=N\,w_d(k,i-k,d-i),\qquad
 w_d(a,b,c)=\frac1{s_as_bs_c},\qquad a+b+c=d.
\]
The symmetric interior maximum is the ideal angle triple
\((x/2,x/2,1-x)\), at the continuum scale. With
\(\Lambda(\theta)=-\int_0^\theta\log(2\sin u)du\),
\[
 \pi B(x)=2\Lambda(\pi x/2)+\Lambda(\pi(1-x))
\]
is its ideal tetrahedron volume. Formula (6) quantifies the actual
overlap of neighboring row packets, including the Fourier phase.
It is a nonzero Gaussian kernel after one explicit diagonal chirp;
it is not obtained by replacing those phases with their magnitudes.

The coefficient \(\sin(\pi a)\) in (6) is unchanged at leading
order by the genuine turn's reflection \(a\mapsto1-a\). The two
fixed endpoint limits likewise have the same moment matrix after
their stated row weights. These facts describe local compatibility
of the kernel. They do not give a global operator inequality for
arbitrarily many rows or an arbitrary sequence of crossings and turns.

In particular no statement here identifies this row covariance with
the full main-color Plancherel energy, the quotient covariance
\(C_E\) of a whole Conway expression, or the original scalar
closing after an unspecified short component. Such an identity or a
controlled composition theorem is still needed before these local
orthogonal frames can prove the finite-exception volume statement.

## Direct sources and written proof check

The author read both complete direct sources and checked the written
finite identities and every asymptotic argument above. The source
hashes used are:

| Source | SHA-256 |
|---|---|
| [Actual crossing and original source](actual_newton_twist_canonical_graph.md) | `387681510416839fd3407f730ab701c7c1c8855b73da66497756721234d4f6d9` |
| [Earlier exact Gaussian frame](research_gaussian_frame_newton_transport.md) | `b6ed7fa19097323f76b0b22fb4fc7361b9d4e52c3f19d17c12d94c6fff623af9` |

The earlier frame note provides exact reconstruction and explicit
crossing kernels, but does not prove the bulk covariance limit or
the two endpoint limits established here. No mathematical program,
test, build or numerical calculation was used in this proof.
