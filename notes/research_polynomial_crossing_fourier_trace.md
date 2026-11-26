# The polynomial crossing and a trace without endpoint currents

Research note, 2 November 2026. The crossing is kept as its original
canonical polynomial in the full pair algebra. This makes the angle
integrand periodic and removes every vertical endpoint current exactly.
There are only finitely many nonzero Fourier charges for any fixed
source network. The crossing polynomial, however, does not have the
same off-grid growth as its Gaussian representative. An explicit
original two-crossing source shows exponential cancellation inside
charge one alone.

The finite trace coefficient identity itself is already proved in
[the zero-power subtree calculation, Section 3](research_zero_power_subtree_fourier_bound.md).
The new statements here are the full-Hermite Fourier coefficients of
an arbitrary signed crossing power, their use in a current-free
network integral, and the source-level cancellation calculation in
Section 5.

## 1. The full crossing polynomial

Let \(N\ge2\), \(D=N-1\), and \(\eta=(-1)^D\). Throughout this note
\(T_N\) is the ordinary Chebyshev polynomial, so that
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 \phi_N(F)=\eta N^2[z^D]\operatorname{rem}_{P_N}F.       \tag{1}
\]
The repeated roots retain their first derivatives. At an odd level
there is also the simple root \(-2\), whose value is retained.

For a signed integer \(n\), including a negative power in the algebra,
write
\[
 r_{n,N}(t)=\operatorname{rem}_{P_N}(R^n)(-2\cos t)
           =\sum_{m=-D}^D b_m e^{imt},\qquad b_{-m}=b_m. \tag{2}
\]
No power is taken pointwise after choosing a representative: the
remainder in (2) is the canonical representative of the algebra power.
Set
\[
 \tau_j=\frac{\pi(D-2j)}N,\quad
 C_{N,n}=\exp\frac{\pi i nD^2}{4N},\quad
 v_j=C_{N,n}\exp\frac{inN\tau_j^2}{4\pi},\quad
 d_j=\frac{inN\tau_j}{2\pi}v_j.                       \tag{3}
\]
The original crossing calculation gives \(r(\tau_j)=v_j\) and
\(r'(\tau_j)=d_j\). The latter is precisely its first normal after
using \(z=-2\cos t\). At the odd simple root \(t=0\), the displayed
derivative is automatically zero and introduces no additional datum.

Define the finite transforms
\[
 V_m=\frac1N\sum_jv_je^{-im\tau_j},\qquad
 W_m=\frac1{iN}\sum_jd_je^{-im\tau_j},\qquad
 T_m=\frac1N\sum_j\tau_jv_je^{-im\tau_j}.              \tag{4}
\]
Then \(W_m=nNT_m/(2\pi)\).

**Proposition 1.** The exact coefficients of the original crossing
polynomial are
\[
 \boxed{\quad b_0=V_0,\qquad
 b_m=\frac{(N-m)V_m+W_m}{N}
     =\left(1-\frac mN\right)V_m+\frac n{2\pi}T_m,
 \quad 1\le m<N.\quad}                               \tag{5}
\]
In particular
\[
 |b_0|\le1,\qquad |b_m|\le1+|n|/2,\qquad
 \sum_{m=-D}^D|b_m|\le B_{n,N}:=1+2D(1+|n|/2).        \tag{6}
\]

**Proof.** Sampling \(e^{ikt}\) on (3) gives zero unless its frequency
is divisible by \(N\); at frequency \(\ell N\) it gives \(\eta^\ell\).
For \(1\le m<N\), the band in (2) therefore gives the two equations
\[
 V_m=b_m+\eta b_{m-N},\qquad
 W_m=m b_m+\eta(m-N)b_{m-N}.                           \tag{7}
\]
Solving gives (5). For \(m=0\) only frequency zero occurs. The data
are even in value and odd in derivative, so the negative coefficients
are the positive ones. These formulas reconstruct both the value and
the derivative at every physical node, hence reconstruct the original
full algebra element. Finally \(|v_j|=1\) and \(|\tau_j|<\pi\), proving
(6). \(\square\)

For completeness, (5) can be written as a literal Hermite interpolation.
Put
\[
 F_N(s)=\frac1N\left(\frac{\sin(Ns/2)}{\sin(s/2)}\right)^2
       =\sum_{|m|<N}(1-|m|/N)e^{ims},\qquad
 J_N(s)=2\sum_{m=1}^{D}\sin(ms).
\]
The removable values of \(F_N\) are understood. Then
\[
 r_{n,N}(t)=\frac1N\sum_jv_jF_N(t-\tau_j)
            +\frac1{N^2}\sum_jd_jJ_N(t-\tau_j).       \tag{8}
\]
Indeed the first summand has the value part of (5). The second has
coefficient \(W_m/N\) at positive frequency and, by oddness of the
sampled derivatives, the same coefficient at negative frequency.
At different grid points \(J_N\) vanishes; its derivative interpolation
matrix is the identity minus the projection onto constants, and
\(\sum_jd_j=0\). Formula (8) is therefore valid at both parities.
The derivative term cannot in general be omitted.

## 2. Exact integrals over a complete period

Let \(f(t,\mathbf u)\) be an even trigonometric polynomial in \(t\),
with arbitrary polynomial dependence on the free boundary variables.
It is kept at its actual degree. Write
\[
 r_{n,N}(t)f(t,\mathbf u)=\sum_k a_k(\mathbf u)e^{ikt},
 \qquad a_{-k}=a_k,
\]
and suppose its degree in \(t\) is at most \(L\). The original trace is
\[
 \phi_N(R^nf)=N^2\sum_{\ell=1}^{\lfloor(L+1)/N\rfloor}
       \ell\eta^{\ell+1}
       \bigl(a_{\ell N-1}-a_{\ell N+1}\bigr).         \tag{9}
\]
To see this directly, the original derivative sampling is
\(
\eta\sum_j(\sin t\,r(t)f(t))'|_{\tau_j}.
\)
The derivative has coefficient
\(k(a_{k-1}-a_{k+1})/2\); pairing the two selected frequencies
\(\pm\ell N\) gives (9). This argument retains all first normals.

For any real height \(h>0\), each coefficient difference in (9) has
the exact integral
\[
 a_{\ell N-1}-a_{\ell N+1}
   =\frac i\pi\int_{-\pi-ih}^{\pi-ih}
          \sin t\,r_{n,N}(t)f(t,\mathbf u)e^{-i\ell Nt}\,dt.
                                                               \tag{10}
\]
The integrand is entire and \(2\pi\)-periodic. The two vertical sides
of a period rectangle are equal with opposite orientations, so there
is no endpoint current in moving (10) from height zero to height
\(-h\). This assertion concerns the polynomial \(r\), not the
nonperiodic function obtained by extending (3) as a Gaussian.

Summing the charges, including the ones whose integrals are zero by
the degree bound, gives another exact formula:
\[
 \boxed{\quad
 \phi_N(R^nf)=\frac{iN^2}{\pi}
   \int_{-\pi-ih}^{\pi-ih}
     \sin t\,r_{n,N}(t)f(t,\mathbf u)
       \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt.
 \quad}                                                     \tag{11}
\]
The geometric series converges uniformly on this contour. Its
coefficient of \(e^{-i\ell Nt}\) is \(\ell\eta^{\ell+1}\), so (11)
is exactly (9). Its infinitely written kernel has only finitely many
nonzero integrals; no asymptotic truncation has occurred.

These identities also hold as identities of the entire unreduced
free-boundary polynomial. They can be iterated in every contracted
variable of the original kernel network. In particular, for a fixed
circle-tree vertex of degree \(d_v\), the product of its incident
kernels and one canonical crossing polynomial has degree at most
\((d_v+1)D\). If \(N>d_v\), only charges \(1,\ldots,d_v\) can occur.
The same degree count applies to identity kernels as to turn kernels.
Thus a fixed network has a bounded number of charge vectors,
independently of \(N\), while preserving all boundary products.
Variables at unfilled vertices are never reduced in this statement.

If the whole product in a contracted variable is first reduced modulo
\(P_N\), only charge one remains. This is exact, but its highest
coefficient then already contains the original trace calculation.
It does not provide a new estimate for that coefficient.

## 3. The polynomial and the Gaussian have different complex growth

The Gaussian representative of the crossing data is
\[
 \chi_{n,N}(t)=C_{N,n}e^{inNt^2/(4\pi)}.                \tag{12}
\]
It agrees with \(r_{n,N}\) in value and first derivative on the
physical grid, but it is not the entire periodic function (2).
Formula (5) specifies the difference exactly: the polynomial combines
two aliased Fourier modes in each residue class, using both the sampled
values and the sampled derivatives. It is a Hermite interpolation of
the Gaussian data, not a periodic Gaussian identity.

There is an explicit exponential obstruction to identifying their
complex-strip growth. For \(n=1\), the original Newton crossing is
\[
 R=\kappa\sum_{k=0}^{D}(-q)^k e_k,\qquad
 q=e^{\pi i/N},\quad\kappa=q^{D^2/2}.
\]
Since the coefficient of \(e^{iDt}\) in \(e_D(-2\cos t)\) is
\(1/N^2\),
\[
 b_D=\frac{\kappa(-1)^Dq^D}{N^2},\qquad |b_D|=N^{-2}. \tag{13}
\]
Fourier coefficient extraction on the line \(t=a-ih\) implies
\[
 \sup_{|a|\le\pi}|r_{1,N}(a-ih)|\ge N^{-2}e^{Dh}.
                                                               \tag{14}
\]
On the same period, 
\(
\sup|\chi_{1,N}(a-ih)|=e^{Nh/2}.
\)
Consequently
\[
 \sup_{|a|\le\pi}|r_{1,N}(a-ih)-\chi_{1,N}(a-ih)|
       \ge N^{-2}e^{Dh}-e^{Nh/2}.                     \tag{15}
\]
At every fixed \(h>0\), the right side eventually has exponential
rate \(h\). This is a global strip statement; it does not locate the
maximum or claim the same discrepancy at \(a=0\).

The explicit upper bound (6) also shows the limitation of a direct
absolute contour estimate. If
\(M_f(h)=\sup_{|a|\le\pi}|f(a-ih,\mathbf u)|\), then (11) gives
\[
 |\phi_N(R^nf)|\le
 \frac{2N^2 B_{n,N}\cosh h\,e^{-h}}{(1-e^{-Nh})^2}
 M_f(h).                                                   \tag{16}
\]
The factor \(e^{Dh}\) from the crossing band has consumed the
\(e^{-Nh}\) first-charge penalty. Higher charges have an additional
\(e^{-(\ell-1)Nh}\), but that observation alone gives no geometric
improvement of the first charge. The next section shows that this
loss is visible in an actual original source.

## 4. A central Fourier difference of the original edge kernel

Let
\[
 K_N(t,0)=\sum_{k=0}^{D}e_k(-2\cos t)e_k(-2)
         =\sum_{m=-D}^{D} c_m e^{imt},\qquad
 M_\infty=4G/\pi,
\]
where \(G\) is Catalan's constant. The full edge theorem, with its
omitted-wire estimates, gives
\[
 K_N(t,0)=\frac14N^{-3/2}e^{NM_\infty}
       \exp\left(-\frac{Nt^2}{4\pi}+O(Nt^4)\right)
       (1+O(N^{-1})+O(t^2))                              \tag{17}
\]
locally at zero, and a strict exponential loss on every fixed closed
part of the real period away from zero. The expansion is used for the
full kernel only after shrinking the local chart and comparing its
selected action with the omitted-wire rate, exactly as in
[the insertion proof](research_twist_period_insertion_growth.md).

**Lemma.** Along both parities,
\[
 c_0-c_2=\pi N^{-3}e^{NM_\infty}(1+O(N^{-1})).          \tag{18}
\]
Here absent coefficients, including \(c_2\) at a small level, are zero.

**Proof.** Evenness gives
\[
 c_0-c_2=\frac1{2\pi}\int_{-\pi}^{\pi}
                  K_N(t,0)(1-\cos2t)\,dt.
\]
All omitted wires and the outer part of the period have a strict loss.
In the remaining interval \(1-\cos2t=2t^2+O(t^4)\), and
\(
\int_{\mathbb R}t^2e^{-Nt^2/(4\pi)}dt=4\pi^2N^{-3/2}.
\)
Substitution in (17) gives (18), including its positive nonzero
constant. Taylor expansion gives the displayed error. \(\square\)

## 5. Exponential cancellation within the only surviving charge

Consider the original two-crossing terminal source
\[
 P_{1,2,N}(0)=\phi_N(R^2K_N(t,0)).                    \tag{19}
\]
The exact two-crossing calculation gives \(\phi_N(R^2)=N\).
By (9), applied to the canonical degree-\(D\) representative alone,
\[
 b_D(r_{2,N})=\frac1N.                                \tag{20}
\]
The product in (19) has degree at most \(2N-2\). Hence charge one is
the only possible charge for every \(N\ge2\):
\[
 P_{1,2,N}(0)=N^2\sum_{m=-D}^{D}
                 b_m(c_{N-1-m}-c_{N+1-m}).             \tag{21}
\]
In this exact finite sum, the individual summand \(m=D\) equals
\[
 N^2b_D(c_0-c_2)
       =\pi N^{-2}e^{NM_\infty}(1+O(N^{-1})).          \tag{22}
\]
The actual terminal theorem, proved from the full original polynomial,
gives instead
\[
 P_{1,2,N}(0)=\frac{e^{-i\pi/4}}2
       \exp\left[N\left(\frac{M_\infty}{2}
                                +\frac{i\pi}{8}\right)\right]
       (1+O(N^{-1})).                                  \tag{23}
\]
See [the two-crossing terminal proof](research_two_crossing_terminal_filling.md),
including its exact normalization.

Thus the other summands in (21) cancel (22) to exponential precision.
Taking absolute values of the crossing-mode summands cannot prove the
correct rate, even though there is only one trace charge and no
endpoint current. This example is an already geometrically identified
short terminal filling, not an artificial choice of coefficients.

For a source with several incident edges the charge-one convolution
still involves at most \(2N-1\) crossing coefficients and two source
coefficients for each of them. A bounded number of charge vectors
therefore does not reduce the problem to a bounded number of positive
or noncancelling contributions. Formula (11) is a useful exact periodic
representation; a general proof must additionally control its
coherent crossing sum or find an equivalent integral that keeps that
cancellation intact.

## 6. Reproduction

Run

~~~sh
python3 experiments/check_polynomial_crossing_fourier_trace.py --output repro/results/research-polynomial-crossing-fourier-trace.json
~~~

The script compares (5), its first derivatives, and the Fourier trace
of a product with two complex free boundary angles against the original
crossing and Newton multiplication matrices. It checks signed powers
\(-3,0,1,2\) at levels \(3,4,5,8\), without dropping any normal.
It also checks the exact highest coefficients (13) and (20).
At six larger levels of both parities it evaluates the full original
kernel coefficients in (22), and evaluates the entire two-crossing
terminal polynomial in (23), including every Newton index.
The [saved results](../repro/results/research-polynomial-crossing-fourier-trace.json)
are finite normalization checks. The asymptotic statements rely on the
proofs above and the cited full edge and terminal estimates.
