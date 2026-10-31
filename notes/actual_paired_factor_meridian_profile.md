# The meridian profile near completeness

31 October 2026.

Fix the quantum parameter \(q_N=e^{\pi i/N}\). The reduced ADO
invariant of the figure-eight knot is a Laurent polynomial
\(f_N(Y)\) in the squared meridian eigenvalue \(Y=M^2\). Its value
at \(Y=1\) is the reduced Kashaev invariant \(K_N\). Here we vary
this meridian while keeping the quantum parameter at its exact root
of unity. Write \(Y=e^{z/N}\), with \(z\) in a fixed compact subset
of the complex plane. We prove

\[
 \frac{f_N(e^{z/N})}{K_N}\longrightarrow
 H(z)=\frac{2\sinh(z/2)}z.
\]

After subtracting the polynomial determined by the ordinary colors
and dividing by their common vanishing factor, the centered regular
profile \(\rho_N\) tends to one. Section 3 gives these operations
explicitly. Both
statements hold through every fixed ordinary-color resonance and
with every fixed derivative. The regularized Laurent polynomial
has the same hyperbolic volume rate there. Its first correction is
\(\tau z^2/(8\pi iN)\), where \(\tau=2\sqrt3\,i\) is the cusp
shape for the preferred meridian and longitude. We obtain that
coefficient from the finite sum and compute the cusp shape separately
from the knot group.

The proof starts from the actual finite cut formula. A general estimate
for paired sine factors is then passed through its positive complete
sum. Section 2 states exactly what would suffice for a signed source;
those contraction hypotheses remain to be established for a general
Conway main-meridian deformation. The parameter \(z\) is fixed before
\(N\) grows. No assertion about a fixed open neighborhood in \(M\)
is obtained by this microscopic scaling.

## 1. Uniform estimates for paired sine products

For \(N\ge2\), \(0\le n<N\), and complex \(z\), put

\[
 P_{N,n}(z)=\prod_{r=1}^{n}
 \left(1+\frac{\sinh^2(z/(2N))}{\sin^2(\pi r/N)}\right),
 \qquad H_N(z)=\frac{\sinh(z/2)}{N\sinh(z/(2N))}.
 \tag{1}
\]

The latter expression has its entire continuation. For every fixed
\(R\), all \(P_{N,n}\) are bounded on \(|z|\le R\), uniformly in
\(N,n\). Indeed \(|\sinh(z/(2N))|\le C_R/N\) and
\(\sin(\pi r/N)\ge2\min(r,N-r)/N\). Hence the product of absolute
values is at most

\[
 \exp\left(C_R\sum_{r=1}^{N-1}
                     \min(r,N-r)^{-2}\right)\le C'_R.
 \tag{2}
\]

For fixed \(0<\delta<1/2\) and all sufficiently large \(N\), there
are holomorphic units \(U_{N,n}\) on \(|z|\le R\) such that

\[
 P_{N,n}=H_N U_{N,n},\qquad
 \sup_{|z|\le R}|U_{N,n}-1|\le C_{R,\delta}/N,
 \quad \delta N\le n\le(1-\delta)N.
 \tag{3}
\]

This is a factorization across the zeros of \(H_N\), rather than
pointwise division by a possibly vanishing value.

To prove it, let \(T_N\) be the monic Chebyshev polynomial determined
by \(T_N(v+v^{-1})=v^N+v^{-N}\). The root factorization of
\(T_N(w)-2\), evaluated at \(w=2\cosh(z/N)\) and divided by its
value after removing the root \(w=2\), gives

\[
 P_{N,N-1}(z)=H_N(z)^2.
 \tag{4}
\]

The normalization uses \(T_N'(2)=N^2\). Factors at \(r\) and
\(N-r\) coincide. Matching values at \(z=0\) therefore proves

\[
 \begin{array}{ll}
 N=2m+1:&P_{N,m}=H_N,\\
 N=2m:&P_{N,m-1}=H_N/\cosh(z/(2N)).
 \end{array}
 \tag{5}
\]

The quotients in (5) are identities of entire functions; on the fixed
disk the displayed cosh is also a unit for large \(N\). Starting at
this midpoint, reach any \(n\) in (3) by multiplying or dividing only
the intervening factors. Every intervening index lies a fixed positive
fraction of \(N\) away from both endpoints. Each factor is consequently
\(1+O_{R,\delta}(N^{-2})\), is a unit on the disk, and there are at
most \(N\) of them. Their product or inverse product is
\(1+O_{R,\delta}(N^{-1})\). The cosh correction in the even case is
\(1+O_R(N^{-2})\). This proves (3). Repeating the estimate on a larger
disk and applying Cauchy's formula gives the same \(O(N^{-1})\)
estimate for each fixed derivative in \(z\).

Also \(H_N\to H\) locally uniformly, with all fixed derivatives and
error \(O(N^{-2})\), where

\[
 H(z)=\frac{2\sinh(z/2)}{z},\qquad H(0)=1.
 \tag{6}
\]

This follows from \(H_N=H\,[z/(2N)]/\sinh(z/(2N))\).

## 2. Passing the estimate through a signed sum

Let \(\Sigma_N\) be a finite set of states and let
\(K_N=\sum_{\sigma}w_{N,\sigma}\ne0\). Suppose the actual deformed
source is exactly

\[
 F_N(z)=\sum_{\sigma\in\Sigma_N}w_{N,\sigma}
                   \prod_{j=1}^{m}P_{N,n_j(\sigma)}(z),
 \tag{7}
\]

with fixed \(m\). Call a state interior if
\(\delta N\le n_j(\sigma)\le(1-\delta)N\) for every \(j\).
Assume constants \(C,c>0\), independent of \(N\), satisfy

\[
 \sum_\sigma|w_{N,\sigma}|\le C|K_N|,
 \qquad
 \sum_{\sigma\text{ not interior}}|w_{N,\sigma}|
                       \le Ce^{-cN}|K_N|.
 \tag{8}
\]

Then, on every fixed complex disk and with every fixed derivative,

\[
 \frac{F_N(z)}{K_N}=H_N(z)^m+O(N^{-1})
                    =H(z)^m+O(N^{-1}).
 \tag{9}
\]

On the interior states, (3) gives a difference from \(H_N^m\) bounded by
\(C_R/N\); (8) bounds its contracted absolute error relative to
\(K_N\). On the other states, (2) bounds both terms uniformly, so
their total error is exponentially small by (8). This proves (9)
as a whole holomorphic estimate; Cauchy's formula on larger disks
proves the derivative statement.

Positivity is one sufficient reason for the first inequality in (8),
but is not assumed in the theorem. The same argument works for an
integral over a specified cycle if the sum of absolute weights is
replaced by its total variation. It is essential to prove these
inequalities for the actual contraction or its exactly equivalent
cycle. An estimate on individual insertions is not (8).

More generally, if the first ratio in (8) is \(\kappa_N\), the proof
gives error \(O_R(\kappa_N/N)\) plus the normalized absolute tail.
Thus \(\kappa_N=o(N)\) is also sufficient for convergence. An
unspecified polynomial bound on \(\kappa_N\) does not suffice for
this first-order estimate.

## 3. The figure-eight knot

The [exact figure-eight source identity](figure_eight_whole_source_identity.md), equation (1.1),
proves directly from the original cut crossings and cups that

\[
 f_N(Y)=\sum_{n=0}^{N-1}\prod_{r=1}^{n}
                       (Y+Y^{-1}-Q_N^r-Q_N^{-r}),
 \qquad Q_N=e^{2\pi i/N}.
 \tag{10}
\]

Put \(Y=e^{z/N}\). Its exact decomposition is

\[
 f_N(e^{z/N})=\sum_{n=0}^{N-1}t_{N,n}P_{N,n}(z),
 \quad t_{N,n}=\prod_{r=1}^{n}4\sin^2(\pi r/N)>0,
 \quad K_N=\sum_{n=0}^{N-1}t_{N,n}.
 \tag{11}
\]

The same source note proves, by monotone Riemann sums at the logarithmic
endpoints,
\(\log t_{N,n}=N\Phi(n/N)+O(\log N)\) uniformly, where
\(\Phi(x)=\int_0^x\log(4\sin^2\pi u)\,du\).
Its unique maximum is at \(x=5/6\). Choose, for example,
\(\delta=1/12\). Compactness gives a fixed positive gap between
this maximum and the complement of \([\delta,1-\delta]\).
A lattice term within \(O(1/N)\) of the maximum supplies the lower
bound for \(K_N\). The polynomial Riemann-sum errors and the at most
\(N\) tail terms are absorbed into a smaller exponential gap.
This proves (8), with \(C=1\) in its first inequality.

Consequently the actual reduced meridian profile satisfies

\[
 g_N(z):=\frac{f_N(e^{z/N})}{K_N}
                  =H_N(z)+O_R(N^{-1})
                  =H(z)+O_R(N^{-1}).
 \tag{12}
\]

The estimate is locally uniform on the whole \(z\)-plane, including
all fixed resonances \(z=2\pi i k\), and holds for every fixed
derivative. It follows from a whole finite source identity, without
using a colored-Jones comparison or a chosen solution of a recurrence.

Let \(P_N^{\mathrm{ord}}\) be the canonical degree-at-most-\(N-2\)
ordinary-color interpolant and
\(R_N=(f_N-P_N^{\mathrm{ord}})/S_N\), with
\(S_N(Y)=1+\cdots+Y^{N-1}\). Retain the full-state centering and put

\[
 \rho_N(z)=e^{(N-1)z/(2N)}
              \frac{N R_N(e^{z/N})}{K_N}.
 \tag{13}
\]

The exact identity is
\(g_N=H_N\rho_N+\pi_N\), where
\(\pi_N=P_N^{\mathrm{ord}}(e^{z/N})/K_N\). The positive volume
growth of (11) and the [polynomial ordinary-color bound](regularized_kashaev_period.md)
imply
\(\pi_N\) and all its fixed derivatives are exponentially small
on every compact disk. For any prescribed disk, choose a larger
boundary circle avoiding the zeros of \(H\). On that circle
\(|H_N|\) is bounded away from zero. The exact numerator
\(g_N-\pi_N-H_N\) is divisible by \(H_N\), so the maximum principle
and (12) prove

\[
 \rho_N(z)=1+O_R(N^{-1})
 \tag{14}
\]

locally uniformly with all fixed derivatives. This is the canonical
regular quotient. The unsubtracted full modified invariant still has
actual poles at ordinary-color resonances; (14) does not remove them
without their specified subtraction.

In particular, for every fixed compact set of \(z\)-values, this
regularized Laurent polynomial has the uniform volume limit

\[
 \frac{2\pi}{N}\log\left|R_N(e^{z/N})\right|
       \longrightarrow\operatorname{Vol}(S^3\setminus4_1).
 \tag{14a}
\]

Indeed (14) is bounded away from zero on that compact set for large
\(N\), and (13) gives
\(R_N(e^{z/N})=K_N e^{-(N-1)z/(2N)}[1+O_R(N^{-1})]/N\).
The centering and the factor \(N^{-1}\) do not change the exponential
rate. The source note identifies the complete rate with the volume
of the actual figure-eight complement. Thus (14a) uses that same
complement, and includes the ordinary-color resonance values of the
regular quotient.

This is a microscopic meridian theorem for the actual figure-eight
source, used as a test of (8). The broad strict Conway volume theorem
does not yet supply (7)–(8) for its main-meridian deformation. Its
auxiliary color estimates leave the main meridian parabolic.

### The first correction

The exact midpoint product also determines the first nonconstant
regular term. Uniformly on the same bulk interval and compact
\(z\)-sets,

\[
 N\bigl(U_{N,n}(z)-1\bigr)
 =-\frac{z^2}{4\pi}\cot(\pi n/N)+O_{R,\delta}(N^{-1}).
 \tag{14b}
\]

Indeed, for every intervening midpoint-to-\(n\) factor,

\[
\log\left(1+\frac{\sinh^2(z/(2N))}{\sin^2(\pi r/N)}\right)
=\frac{z^2}{4N^2}\csc^2(\pi r/N)+O_{R,\delta}(N^{-4}).
\]

The signed sum of these logarithms is a Riemann sum from \(1/2\)
to \(n/N\); its integral is \(-\cot(\pi n/N)/\pi\). The
midpoint offset and the even cosh correction contribute
\(O(N^{-2})\) before multiplying by \(N\). Exponentiating gives
(14b), as a whole holomorphic estimate.

The positive probability weights \(t_{N,n}/K_N\) concentrate at
\(5/6\). On the bulk interval the cotangent is bounded, so its
weighted mean tends to \(-\sqrt3\). The exponentially small tails
remain negligible after multiplication by \(N\). Equations
(11) and (14b) therefore give
\(N(g_N-H_N)-H_N\sqrt3 z^2/(4\pi)\to0\) locally uniformly.
Subtract \(N\pi_N\) and divide on the same fixed boundary circles
as above. The quotient is entire before applying the maximum
principle. Hence

\[
 N\bigl(\rho_N(z)-1\bigr)
       \longrightarrow \frac{\sqrt3}{4\pi}z^2
 \tag{14c}
\]

locally uniformly with every fixed derivative. Since \(\rho_N\)
is close to one on each fixed disk, its logarithm there satisfies
the same first-order limit. In particular
\(N(\log\rho_N)''(0)\to\sqrt3/(2\pi)\).

### Why the coefficient is the cusp shape

We compute the peripheral curves with their orientations, since the
sign of the coefficient cannot be read from an unmarked polynomial.
Use the braid \((\sigma_1\sigma_2^{-1})^2\) for the figure-eight knot
and the meridian matrices

\[
A=\begin{pmatrix}M&1\\0&M^{-1}\end{pmatrix},\qquad
B=\begin{pmatrix}M&0\\t&M^{-1}\end{pmatrix},\qquad
C=A^{-1}BAB^{-1}A.
\]

The braid closure gives
\(t^2+(M^2+M^{-2}-3)t+3-M^2-M^{-2}=0\).
Put \(D=A^{-1}BA\) and \(E=CAC^{-1}\). The successive meridian
triples under the four crossings are

\[
(A,B,C),\quad(D,A,C),\quad(D,C,E),\quad
(D^{-1}CD,D,E),\quad(D^{-1}CD,E,EDE^{-1}).
\]

The closure relation reduces the final triple to \((A,B,C)\).
Track each original strand through the crossings: its accumulated
underpass transport is respectively \(C\), \(BA^{-1}\), and
\(D^{-1}\). Following the closed knot visits these strands in that
order, so the transport is \(W=D^{-1}BA^{-1}C\).
The writhe is zero. With the preferred-longitude convention of the
[peripheral calculation](quantum_longitude_and_regulator_action.md),
the longitude is
\(\lambda=W^{-1}=C^{-1}AB^{-1}A^{-1}BA\).

At \(M=1\), direct multiplication using \(t^2-t+1=0\) gives

\[
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
\lambda=\begin{pmatrix}-1&4t-2\\0&-1\end{pmatrix}.
\]

The meridian translates the boundary plane by one. The projective
action of the longitude translates it by \(2-4t\). The
[positive Bloch specialization](figure_eight_bloch_specialization.md)
selects \(t=(1-\sqrt3\,i)/2\), paired with the ideal tetrahedron
shape \((1+\sqrt3\,i)/2\) in the upper half-plane. Thus the oriented
cusp shape is \(\tau=2-4t=2\sqrt3\,i\).

The preferred longitude lift still has eigenvalue \(-1\) at
completeness. To check its variation without dropping that sign,
the upper-left entry of the same matrix word is

\[
L_{\mathrm{intr}}(M)
=M^4-2M^2-1+M^{-2}+(M^2-M^{-2})t(M).
\]

It satisfies \(L_{\mathrm{intr}}(1)=-1\) and
\(\left.d\log L_{\mathrm{intr}}/d\log M\right|_{M=1}=2-4t=\tau\).
Centering the longitude as \(\ell=-L_{\mathrm{intr}}\) changes
neither this derivative nor the recorded sign of its lift.
In the squared coordinates \(U=2\log M\), \(V=2\log\ell\),
the ratio \(dV/dU\) is again \(\tau\).

Consequently the coefficient proved from the finite sum is

\[
N(\rho_N(z)-1)\longrightarrow\frac{\tau}{8\pi i}z^2,\qquad
N\rho_N''(0)\longrightarrow\frac{\tau}{4\pi i}.
\]

Here \(M=e^{z/(2N)}\). Both this scale and the primitive peripheral
curves are needed for the factor \(8\pi i\). The calculation proves
the match for this knot; it does not infer an analogous asymptotic
for other knots merely from their peripheral equations.

### Illustration and reproduction

![Finite figure-eight meridian profiles at levels 24, 47 and 80, together with the limiting sine profile and the error after ordinary-color subtraction.](../book/figures/figure-eight-meridian-profile.png)

Set \(z=it\) with real \(t\). The left panel compares
\(g_N(it)=f_N(e^{it/N})/K_N\) with
\(H(it)=2\sin(t/2)/t\). The right panel shows
\(\lvert\rho_N(it)-1\rvert\). At \(t=\pm2\pi,\pm4\pi\), the
displayed quotient for \(\rho_N\) has a removable zero in both
numerator and denominator. The values plotted there use their
derivatives, as required by the definition of the regular quotient.
The proof above applies on every fixed complex compact set; the
figure shows one real slice.

Run the [plot script](../experiments/plot_figure_eight_meridian_profile.py)
to regenerate the PDF, SVG, PNG and
[finite numerical data](../experiments/figure_eight_meridian_profile_plot.json):

~~~sh
python3 experiments/plot_figure_eight_meridian_profile.py
~~~

The script evaluates the finite sum and its specified interpolant.
The plotted curves are illustrations of the theorem.

## 4. Individual shifted factorials

There is a useful more general local calculation. For
\(\delta N\le n\le(1-\delta)N\), let

\[
 A_{N,n}(s)=\prod_{r=1}^{n}
                 \frac{\sin(\pi(r+s)/N)}{\sin(\pi r/N)}.
 \tag{15}
\]

Uniformly for \(s\) in any fixed compact complex set,

\[
 A_{N,n}(s)=
 \frac{[N\sin(\pi n/N)/\pi]^s}{\Gamma(1+s)}
                         V_{N,n}(s),
 \qquad V_{N,n}=1+O(N^{-1}).
 \tag{16}
\]

Here the positive real base fixes its logarithm. The factor \(V\)
is a holomorphic unit, including at negative integers where the
reciprocal Gamma factor vanishes, for all sufficiently large \(N\).
Each fixed derivative of \(V-1\) has the same bound.

For a direct proof, separate each sine into its linear factor and
\(\operatorname{sinc}\). Euler's product for Gamma, with its tail
estimated by \(\sum_{r>n}O_R(r^{-2})\), gives

\[
 \prod_{r=1}^{n}\frac{r+s}{r}
       =\frac{n^s}{\Gamma(1+s)}[1+O_R(n^{-1})].
 \tag{17}
\]

One first removes the finitely many factors whose zeros lie in the
chosen compact set. The remaining logarithms have no zero there,
so (17) is a holomorphic-unit estimate through those zeros as well.
The harmonic-sum correction \(H_n-\log n-\gamma=O(1/n)\) and the
convergent logarithmic tail justify the bound without assuming the
ratio is nonzero at a Gamma pole.

Now \(b(t)=\log[\sin(\pi t)/(\pi t)]\) is holomorphic on a fixed
complex neighborhood of \([0,1-\delta]\), with \(b(0)=0\).
Taylor expansion and a Riemann-sum estimate yield

\[
 \sum_{r=1}^{n}\bigl[b((r+s)/N)-b(r/N)\bigr]
       =s\,b(n/N)+O_{R,\delta}(N^{-1}).
 \tag{18}
\]

Exponentiating (18) and combining with (17) proves (16).
It explains the paired result: set \(s=z/(2\pi i)\) and multiply
the shifts \(s,-s\). Their powers of \(N\sin(\pi n/N)/\pi\)
cancel, and
\(1/[\Gamma(1+s)\Gamma(1-s)]=\sin(\pi s)/(\pi s)=H(z)\).
The exact midpoint argument additionally retains \(H_N\) and its
finite-level resonance zeros.

For a finite product of shifted factors with shifts \(a_j s\) and
integer powers \(\varepsilon_j\), (16) shows explicitly that the
power of \(N\) is \(s\sum_j\varepsilon_j a_j\). It cancels when
that signed sum is zero. The remaining leading multiplier is

\[
 \prod_j\Gamma(1+a_js)^{-\varepsilon_j}
 \exp\left(s\sum_j\varepsilon_j a_j
                     \log[\sin(\pi x_j)/\pi]\right),
 \quad x_j=n_j/N.
 \tag{19}
\]

When negative powers occur, this statement is made first on compact
sets avoiding the denominator zeros; any continuation across them
must be justified in the original whole source. Formula (19) does
not by itself identify its exponential with a longitude or its
Gamma factor with the single-knot factor \(H\). Those are explicit
source and geometric matching obligations. Likewise, the local
factorial estimate does not supply the contraction estimate (8).

## Relation to earlier asymptotic questions

Colored Alexander asymptotics for the figure-eight knot were
already studied by Cho and Jun Murakami in
[*Some limits of the colored Alexander invariant of the figure-eight
knot and the volume of hyperbolic orbifolds*](https://doi.org/10.1142/S0218216509007464).
The statement proved here fixes \(q_N\) at its exact root and varies
the main color by a bounded complex offset, then retains the
canonical ordinary-color subtraction and every fixed derivative.
The available bibliographic check did not settle whether this
precise normalized profile appears in that earlier work. No
priority claim is made. The proof here is the finite-product and
concentration argument given above.
