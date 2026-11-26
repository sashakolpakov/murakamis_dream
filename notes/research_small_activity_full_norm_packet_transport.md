# Norm bounds and coherent packets for finite Euler operators

22 November 2026. Research note.
Earlier final notes and public manuscripts remain unchanged.

The actual finite Euler operators have explicit norm and inverse-norm
bounds at every activity. At small activities, the compact coherent
composition theorem also implies a full physical vector estimate.
Its local generating kernel, reconstructed through
the exact coherent frame, approximates the actual output in relative
norm \(O(N^{-1})\). The entire complementary coherent window is
exponentially small in that same norm. This is stronger than testing
the output against one coherent row.

The norm bounds hold at every complex activity. The coherent packet
approximation requires small activities. Neither assertion identifies
the original closed-source coefficient for arbitrary signed crossings.

## 1. Actual head spaces and words

Fix the number \(r\) of physical heads. Put
\[
 N\ge2,\qquad d=N-1,\qquad Q=e^{2\pi i/N},\qquad
 x=-e^{-\pi i/N},\qquad F_n=(Q;Q)_n .
\]
Let \(V_N\) have basis \(w_0,\ldots,w_d\) and positive metric
\[
 \|w_a\|^2=\binom da^{-1},\qquad
 \mathcal V_N=V_N^{\otimes r}.
 \tag{1}
\]
This is the binomial **head metric**, not the Newton pair-algebra
coefficient metric used in the Conway quartic.

At the complete meridian use the literal matrices
\[
 Ew_a=(Q^{-a}-1)w_{a-1},\quad Ew_0=0,\qquad
 Kw_a=xQ^{-a}w_a,
\]
and set
\[
 X_i=E_iK_{i+1}\cdots K_r,\qquad
 U_{i,N}(\lambda)=\sum_{n=0}^{d}\frac{\lambda^nX_i^n}{F_n}.
 \tag{2}
\]
In particular \(X_i^N=0\); no extreme arrow is made cyclic.
Choose a fixed finite ordered list \(i_1,\ldots,i_\ell\), allowing
repetitions, and define
\[
 W_N(\boldsymbol\lambda)
   =U_{i_\ell,N}(\lambda_\ell)\cdots U_{i_1,N}(\lambda_1).
 \tag{3}
\]
The list and the activities are fixed before \(N\) varies. Activities
are arbitrary in Section 2 and restricted to a sufficiently small
fixed polydisk for the coherent packet theorem.

Write \(Y=(\mathbb P^1)^r\). In an affine chart the normalized
coherent head vector and probability measure are
\[
 \psi_z=(1+|z|^2)^{-d/2}
             \sum_{a=0}^{d}\binom da z^a w_a,\qquad
 d\mu(z)=\frac{d\Re z\,d\Im z}{\pi(1+|z|^2)^2}.
 \tag{4}
\]
On several heads take tensor products, denoted again by \(\psi_z\),
and use \(d\mu^{[r]}\). Coherent vectors are specified up to unit
phase on projective overlaps. All formulas below transform
covariantly; one may choose measurable phases for the integrals.

## 2. Exact norm bounds at every activity

Write \(\mathcal E_N(T)=\sum_{n=0}^{d}T^n/F_n\).
For every complex \(\lambda\), every \(N\ge2\), and every head \(i\),
\[
 \boxed{\quad
 \|U_{i,N}(\lambda)^{\pm1}\|\le(1+|\lambda|)^d,\qquad
 \|\mathcal E_N(\lambda X)^{\pm1}\|
                      \le(1+|\lambda|)^{rd},\quad X=\sum_iX_i .
 \quad}
 \tag{5}
\]
Both assertions concern the original binomial metric.

To prove the first, \(E^n/F_n\) is one strict shift. On input \(w_a\),
its coefficient for \(a\ge n\) is a unit phase times
\({a\brack n}_Q\), and it is zero for \(a<n\).
The recurrence
\({a\brack n}_Q={a-1\brack n-1}_Q+Q^n{a-1\brack n}_Q\),
with boundary coefficients one, proves that this is a polynomial
in \(Q\) with nonnegative integer coefficients, whose
value at \(Q=1\) is \(\binom an\). Hence its modulus on \(|Q|=1\)
is at most \(\binom an\). In the orthonormal basis its coefficient
therefore has modulus at most
\[
 \binom an\sqrt{\frac{\binom da}{\binom d{a-n}}}
       =\sqrt{\binom an\binom{d-a+n}{n}}\le\binom dn .
\]
Taking the largest strict-shift coefficient gives
\(\|E^n/F_n\|\le\binom dn\).
The Cartan tails in \(X_i^n\) are unitary, giving the same bound.
Summing proves \(\|U_{i,N}(\lambda)\|\le(1+|\lambda|)^d\).

The inverse finite Euler polynomial is exactly
\[
 \mathcal E_N(T)^{-1}
     =\sum_{n=0}^{d}
            \frac{(-1)^nQ^{n(n-1)/2}T^n}{F_n},
                       \qquad T^N=0.
\]
Indeed the product coefficient of \(T^m\), \(0<m<N\), is
\(F_m^{-1}\sum_{n=0}^m(-1)^nQ^{n(n-1)/2}{m\brack n}_Q=0\),
by the finite binomial product containing \(1-1\). Its extra
coefficients vanish by \(T^N=0\). All inverse coefficient multipliers
have modulus one, proving the inverse bound.

For the total \(X\), one has \(X_iX_j=QX_jX_i\) when \(i<j\).
The ordered finite \(q\)-multinomial identity gives, for \(n<N\),
\[
 \frac{X^n}{F_n}=
   \sum_{n_1+\cdots+n_r=n}
          \frac{X_r^{n_r}\cdots X_1^{n_1}}{F_{n_r}\cdots F_{n_1}},
 \qquad
 \left\|\frac{X^n}{F_n}\right\|
      \le\sum_{n_1+\cdots+n_r=n}\prod_i\binom d{n_i}
      =\binom{rd}{n}.
\]
The ordered identity follows by induction using the displayed
\(q\)-commutations; the final equality is ordinary Vandermonde.
At the primitive root \(X^N=0\), as in the source theorem.
The same inverse polynomial now proves the second bound in (5).

In particular the actual word (3) obeys, at all activities,
\[
 \|W_N^{\pm1}\|\le\prod_{j=1}^{\ell}(1+|\lambda_j|)^d,\qquad
 \|W_Nv\|\ge
           \prod_{j=1}^{\ell}(1+|\lambda_j|)^{-d}\|v\|.
 \tag{6}
\]
These exact budgets do not assert a large-activity WKB kernel.

## 3. The exact frame and the two small-activity estimates

The coherent analysis map is
\[
 (\mathcal A_Nv)(y)=\langle\psi_y,v\rangle,\qquad
 \mathcal A_N:\mathcal V_N\longrightarrow
                     L^2(Y,N^r\,d\mu^{[r]}).
\]
It is an isometry, and its adjoint is
\[
 \mathcal A_N^*f=N^r\int_Y\psi_y f(y)\,d\mu^{[r]}(y),
 \qquad \mathcal A_N^*\mathcal A_N=I,\quad
                         \|\mathcal A_N^*\|=1.
 \tag{7}
\]
Indeed angular integration makes the one-head resolution diagonal.
Its \(a\)-th diagonal coefficient in the orthonormal basis is
\[
 \binom da\int_0^\infty
                 \frac{t^a}{(1+t)^{N+1}}\,dt=\frac1N.
\]
The substitution \(u=t/(1+t)\) and repeated integration by parts
give the integral \(a!(d-a)!/N!\). Tensoring proves (7).

Fix a compact set \(Z\subset Y\) of input positions, and use the maximum
of the head Fubini--Study distances for \(\operatorname{dist}\). Choose a small
fixed projective radius \(\varepsilon>0\), so that each pair
\((y,z)\), \(z\in Z\), \(\operatorname{dist}(y,z)<3\varepsilon\),
lies in a nonincident local chart from the compact composition theorem.
A finite projective chart cover suffices. For each \(z\), select one
chart valid on its whole radius-\(3\varepsilon\) window, and use that
chart's phase and coefficient throughout the construction.
All constants and the activity radius are uniform on this finite cover.
No exact gluing of different local leading phases is assumed.

Put \(v_N=W_N\psi_z\) and \(k_N(y,z)=\langle\psi_y,v_N\rangle\).
The compact composition theorem supplies its actual local kernel:
\[
 \begin{split}
 k_N(y,z)&=k_N^{\mathrm{app}}(y,z)(1+R_N(y,z)),\\
 k_N^{\mathrm{app}}(y,z)
   &=\langle\psi_y,\psi_z\rangle
       e^{N\mathcal S(\boldsymbol\lambda,\bar y,z)}
                       b(\boldsymbol\lambda,\bar y,z),\\
 |R_N|&\le C/N,\qquad
 \mathcal S(0)=0,\quad b(0)=1.
 \end{split}
 \tag{8}
\]
The coefficient \(b\) is a holomorphic unit. The estimate is uniform
on the stated local pairs and a sufficiently small activity polydisk.
The overlap in (8) is kept to its exact degree \(d=N-1\).
The local coherent section convention is used on the selected chart.

There is also an absolute off-diagonal estimate on the full sphere:
after shrinking the activity polydisk,
\[
 |k_N(y,z)|\le Ce^{-cN}
       \quad\text{if }\operatorname{dist}(y,z)\ge\varepsilon.
 \tag{9}
\]
Here and below positive constants may change between formulas.
To see explicitly that the source theorem gives (9), insert its exact
coherent resolutions between the factors in (3). A chain whose
endpoints have distance at least \(\varepsilon\) has a consecutive
pair separated by at least \(\varepsilon/\ell\), in at least one
head, by the triangle inequality. The global separated-link estimate
(18) of that theorem bounds this factor by \(Ce^{-c_0N}\).
Its global estimate (17) bounds every other link by
\(Ce^{C_0N\max_j|\lambda_j|}\). Reduce the activities to absorb
the finitely many latter costs. The probability measures have mass
one, and the exact resolution factor \(N^{r(\ell-1)}\) is absorbed
by reducing \(c\). This includes cross-pair incidence and both
coordinate poles. For \(\ell=1\) it is precisely its estimate (18).

Fix the gap \(c>0\) in (9) on an initial small activity polydisk.
Shrink it once more so that
\(\sum_j\log(1+|\lambda_j|)\le c/4\).
The exact inverse bound (6) then gives
\[
                     \|v_N\|\ge e^{-cN/4}.
 \tag{10}
\]
Thus the absolute error in (9) is
exponentially small relative to the actual output norm.

## 4. Reconstruction gives a full-norm approximation

Choose \(0\le\chi_z\le1\), equal to one on the radius-\(\varepsilon\)
window about \(z\), and supported in its radius-\(2\varepsilon\)
window. Define the actual vector
\[
 \boxed{\quad
 v_N^{\mathrm{app}}
    =\mathcal A_N^*
                  \bigl(\chi_z k_N^{\mathrm{app}}(\,\cdot\,,z)\bigr).
 \quad}
 \tag{11}
\]
Thus it is a polynomial section of degree at most \(d\) in each
head, rather than an unextended local WKB germ. Its construction
uses the specified phase, amplitude, cutoff and exact finite frame.
It does not use the value of a knot invariant.

**Theorem.** For the fixed words (3), a sufficiently small activity
polydisk, all \(z\in Z\), and every sufficiently large integer \(N\),
\[
 \boxed{\quad
 \|W_N\psi_z-v_N^{\mathrm{app}}\|
       \le \bigl(C/N+Ce^{-c_2N}\bigr)\|W_N\psi_z\|.
 \quad}
 \tag{12}
\]
The exact positive coherent mass outside the smaller window satisfies
\[
 \boxed{\quad
 N^r\int_{\operatorname{dist}(y,z)\ge\varepsilon}
       \frac{|k_N(y,z)|^2}{\|W_N\psi_z\|^2}\,d\mu^{[r]}(y)
                                  \le Ce^{-c_2N}.
 \quad}
 \tag{13}
\]

**Proof.** Since (8) is relative and \(C/N<1/2\), it implies
\(|k_N-k_N^{\mathrm{app}}|\le (2C/N)|k_N|\) on the support
of \(\chi_z\). The exact decomposition is
\[
 k_N-\chi_zk_N^{\mathrm{app}}
   =\chi_z(k_N-k_N^{\mathrm{app}})+(1-\chi_z)k_N .
 \tag{14}
\]
Its first term has \(L^2(Y,N^r d\mu^{[r]})\) norm at most
\((2C/N)\|v_N\|\), by (7). Equations (9)--(10) give for the second
term a bound \(CN^{r/2}e^{-cN}/\|v_N\|\le Ce^{-c_2N}\)
after division by \(\|v_N\|\). Apply the contraction
\(\mathcal A_N^*\) in (7) to (14). This proves (12).
Squaring (9), integrating, and using (10) proves (13), after reducing
\(c_2>0\). All finite coefficients were included before either
estimate was taken. \(\square\)

For example the positive partial resolution
\[
 P_{\Omega_z}=N^r\int_{\operatorname{dist}(y,z)<\varepsilon}
                         |\psi_y\rangle\langle\psi_y|\,d\mu^{[r]}
\]
satisfies \(0\le P_{\Omega_z}\le I\). Formula (13) is exactly
\(\langle u_N,(I-P_{\Omega_z})u_N\rangle\le Ce^{-c_2N}\),
where \(u_N=v_N/\|v_N\|\); it also bounds
\(\|(I-P_{\Omega_z})u_N\|^2\). This is a fixed small window,
chosen before shrinking activities, not a claim of a window
centered at \(z\) with radius \(N^{-1/2}\).

For large \(N\), (12) makes \(v_N^{\mathrm{app}}\ne0\).
Writing \(u_N^{\mathrm{app}}=v_N^{\mathrm{app}}/
\|v_N^{\mathrm{app}}\|\), normalization gives
\[
 \|u_N-u_N^{\mathrm{app}}\|\le C/N+Ce^{-c_2N},\qquad
 \bigl\||u_N\rangle\langle u_N|
       -|u_N^{\mathrm{app}}\rangle\langle u_N^{\mathrm{app}}|\bigr\|_1
                              \le C/N+Ce^{-c_2N}.
 \tag{15}
\]
Indeed normalization costs at most twice the relative error;
the trace norm of the projector difference is at most twice the
distance of the unit vectors.

## 5. What has and has not been composed

The estimates concern a whole fixed small-activity word. They do
not assert that the output is another single coherent vector.
Nor are they obtained by passing an \(O(N^{-1})\) vector error
through successive exponentially large operator norms: the source
theorem composes the actual kernels first and pays their whole
compact complement before (11) is formed.

All original zero endpoint arrows, root carries and finite head
coefficients used by that theorem are retained. Equation (14)
keeps the exact outside contribution before estimating it. In
particular any physical endpoint coefficient has the absolute
error furnished by (12). It need not have a small relative error:
an exponentially small prescribed closing can be smaller still.
No endpoint atom or source current is declared identically zero.
The statement is at the fixed root and complete meridian; it does
not estimate meridian or quantum-parameter derivatives of the
vacuum walls by differentiating this root theorem.

Small activity is essential for the packet approximation, even though
(5)--(6) hold everywhere. For example the one-head normalized
argument is \(t=\lambda z/(1+wz)\). Under a covariant diagonal
frame change \(D=\operatorname{Sym}^d\operatorname{diag}(a,b)\),
one has \(D^{-1}ED=(b/a)E\), while the input coordinate changes
inversely; the combination \(t\) is unchanged. Merely making the
displayed coefficient smaller by a diagonal gauge does not put
a physical activity-one crossing in the proved domain.

Finally \(\mathcal V_N\) is a tensor of physical heads. No uniformly
conditioned reconstruction into the full Newton pair-algebra
coefficient metric, or through the modified cut and opposite-source
quotient, is supplied here. Thus (12) is not itself the quartic
Newton recursion-residual estimate. General signed crossings,
turnovers, arbitrary short-filling geometric-chart membership,
and the nonzero original closing after branching remain additional
source estimates. No volume lower bound or new filling class is claimed.

## Complete proof source and coverage

The entire matching proof source was read:

| Source | SHA-256 |
|---|---|
| [Actual compact coherent composition](research_capped_coproduct_compact_coherent_composition.md) | c54ba609e91ca18193ac9c9d7e7b32f0d0b39c00b3ff36bdf830184f8ad24d2b |

Its actual definitions, local kernel theorem and global separated-link
estimates are the inputs. The all-activity operator bounds, tight-frame
identity and the passage
to a relative full-norm estimate are proved above. This is a
consequence of established coherent-frame methods, not a new
small-activity kernel asymptotic. Only written mathematics and
text/hash operations were used; no code, mathematical test, build,
git operation or earlier-final edit was performed.
