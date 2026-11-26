# Factorial chambers for the actual Newton gates

Private written proof, 15 November 2026.

The canonical factorial already has uniform asymptotics on compact
subsets of both open half-planes, without a restriction on the real
part. Near a real noninteger argument outside its original strip,
the missing factors are explicit level-dependent Fourier factors.
Retaining them gives a local meromorphic normal form for every
algebraically regular multiplication or signed-crossing gate.

For any collection of nonconstant wrapped real-affine arguments, a common
imaginary direction puts their Fourier factors and inverse factors
in a pointed cone. Their joint constant Fourier coefficient is then
exactly one, even if the affine forms are dependent. This concerns
the distinguished sector of that specified chamber. A previously
marked geometric action can differ by a Fourier character; its
sector is not relabeled as the constant one. Nothing here computes
the coefficient of the original integration cycle.

## 1. Exact periods and marked primitives

The canonical sine factorial is the original function
\[
 G_N(z)=\left(\frac{2\pi}{N}\right)^z\Gamma(z+1)
 \prod_{r\ge1}
  \frac{\Gamma(Nr+z+1)}
       {\Gamma(Nr-z)(Nr)^{2z+1}}.
 \tag{1}
\]
Its positive-base powers use real logarithms. The source construction
proves its nonvanishing on \(-1<\Re z<N\), its meromorphic continuation,
and the exact identities
\[
 G_N(z+1)=2\sin\frac{\pi(z+1)}N\,G_N(z),\qquad
 G_N(z)G_N(N-1-z)=N.
 \tag{2}
\]
In particular, the complementary displacement is \(N-1\), not \(N\).

For \(\tau=+1\), on the upper half-plane put
\[
 J_+(\xi)=\frac{i\pi}{2}\xi(1-\xi)
       +\frac{i}{2\pi}
          \{\operatorname{Li}_2(e^{2\pi i\xi})-\pi^2/6\};
 \qquad J_-(\xi)=\overline{J_+(\bar\xi)}.
 \tag{3}
\]
The dilogarithm in its defining half-plane is its convergent disk
series. Both primitives agree with the original \(J\), real on
\(0<\xi<1\), on their overlaps with \(0<\Re\xi<1\). Their continuations
satisfy, for every integer \(k\),
\[
 \begin{split}
 J_\tau(\xi+k)
    &=J_\tau(\xi)-\tau\pi i
                      \{k\xi+k(k-1)/2\},\\
 J_\tau'(\xi+k)&=J_\tau'(\xi)-\tau\pi i k.
 \end{split}
 \tag{4}
\]
These identities follow by differentiating (3) and fixing the
constant there; the integer shifts leave its disk variable unchanged.

The finite sine product in (2) gives
\[
 G_N(z+N)=-2\sin(\pi z)\,G_N(z).
 \tag{5}
\]
Iterating in either direction, as meromorphic identities, gives
\[
 G_N(z+kN)
  =(-1)^{Nk(k-1)/2}[-2\sin(\pi z)]^kG_N(z),
                         \qquad k\in\mathbb Z.
 \tag{6}
\]
This formula retains its zeros and poles. For negative \(k\),
the displayed power is a reciprocal; it is not replaced by a
nonvanishing normalization.

## 2. A uniform normal form through a real chamber

Fix an integer \(k\), a compact set in \(k<\Re\xi<k+1\), and a
bounded complex offset \(a\). For \(\tau=\pm1\), extend \(J_\tau\)
to this strip from its indicated half-plane, using (4) and the
original primitive at \(\xi-k\). Define
\[
 \mathcal U_N(\xi,a)=
 \frac{G_N(N(\xi-k)+a)}
 {N^{1/2}\exp\{NJ(\xi-k)+(a+\tfrac12)J'(\xi-k)\}}.
 \tag{7}
\]
For all sufficiently large \(N\), this is a nonzero holomorphic
function on a fixed neighborhood of the compact set. The original
uniform strip expansion proves
\[
 \mathcal U_N(\xi,a)=1+O_{\rm hol}(N^{-1}).
 \tag{8}
\]
Every fixed derivative has this order on smaller compact sets,
also with respect to bounded offsets on a fixed compact set.

**Theorem 1.** With the same actual offset and either choice of
\(\tau\), the following identity is exact and meromorphic:
\[
 \boxed{\quad
 G_N(N\xi+a)=
 N^{1/2}\exp\{NJ_\tau(\xi)+(a+\tfrac12)J_\tau'(\xi)\}
 \bigl(1-e^{\tau2\pi i(N\xi+a)}\bigr)^k
 \mathcal U_N(\xi,a).
 \quad}
 \tag{9}
\]
Consequently (8) is a uniform asymptotic after the displayed
Fourier divisor has been factored, including at its zeros and
poles. The remainder is not differentiated by first dividing
pointwise at a zero; it is the holomorphic function (7).

**Proof.** Apply (6) with \(z=N(\xi-k)+a\). For either sign,
\[
        -2\sin\pi z
       =-\tau i\,e^{-\tau\pi i z}
                       (1-e^{\tau2\pi i z}).
 \tag{10}
\]
The last factor is unchanged by adding \(kN\).
Substitute (7) and use (4). The remaining constant is
\[
 (-1)^{Nk(k-1)/2}
 e^{\tau\pi iNk(k-1)/2}
 (-\tau i)^k e^{\tau\pi i k/2}=1.
 \tag{11}
\]
Indeed \(k(k-1)\) is even. Thus no parity scalar, square-root
sign or offset phase is missing from (9). The uniform remainder
claim is precisely the original strip estimate applied in (7).
This proves the theorem. \(\square\)

On a compact set with \(\tau\Im\xi>0\), the Fourier factor in
(9) is \(1+O(e^{-cN})\), with every fixed derivative after
possibly decreasing \(c>0\). This recovers the archived
half-plane asymptotic. If \(\Re\xi\) is an integer but
\(\Im\xi\ne0\), that half-plane theorem applies directly,
without a real-chamber choice.

At a real argument outside \((0,1)\), the factor in (9) cannot
in general be dropped. Its zero or pole lattice is
\(N\xi+a\in\mathbb Z\), with signed order \(k\). Nonvanishing
of \(\sin(\pi\xi)\) excludes the macroscopic factorial wall,
not this level-dependent lattice.

Both signs give the same exact function, not different
interpolations. Their agreement is also visible from
\[
 1-e^{2\pi iz}=-e^{2\pi iz}(1-e^{-2\pi iz})
 \tag{12}
\]
together with (4). Exponentially small Fourier factors in one
half-plane need not be small in the other one.

## 3. The literal multiplication and crossing factors

For actual index variables \(I,J,R\), retain the canonical
interpolation of the original multiplication coefficient:
\[
 \mu_N(I,J,R)=
 \frac{G_N(I+J)G_N(R)}
 {G_N(I)G_N(J)G_N(R-I)G_N(R-J)G_N(I+J-R)}.
 \tag{13}
\]
On its original supported integer set this is the exact positive
Newton multiplication table, including the original repeated-root
algebra. Its seven scaled arguments and multiplicities are
\[
 \begin{array}{c|rrrrrrr}
 \ell_j&x+y&z&x&y&z-x&z-y&x+y-z\\ \hline
 \nu_j&1&1&-1&-1&-1&-1&-1 .
 \end{array}
 \tag{14}
\]
If \(I=Nx+a_I,\ J=Ny+a_J,\ R=Nz+a_R\), their literal offsets
are respectively
\[
 a_I+a_J,\ a_R,\ a_I,\ a_J,\ a_R-a_I,\ a_R-a_J,\
                                      a_I+a_J-a_R.
 \tag{15}
\]
No offset is rounded or removed.

For a signed crossing \(\sigma=\pm1\), use the specified
interpolation of the actual multiplication matrix, with output
\(I\) and input \(J\):
\[
 (M_{\sigma,N})_{I,J}
   =\kappa_N^\sigma
       e^{\sigma\pi i I}
       e^{\sigma\pi i I(J+1)/N}
       \frac{G_N(I)}{G_N(J)G_N(I-J)},\qquad
 \kappa_N=e^{\pi i(N-1)^2/(2N)}.
 \tag{16}
\]
The sign interpolation \(e^{\sigma\pi iI}\) is the original
one used for this signed local phase. The boundary operator
\(C_{\sigma,N}\) is the transpose of (16). The three factorial
arguments are \(x,y,x-y\), of multiplicities \(1,-1,-1\),
with offsets \(a_I,a_J,a_I-a_J\). The complete prefactor in
(16) is retained exactly.

At any point where all seven sines in (14), or all three
crossing sines, are nonzero, choose a small fixed neighborhood.
An argument with \(k_j<\Re\ell_j<k_j+1\) has the period chart
(9), whether it is real or nonreal. A nonreal argument may
instead use the archived half-plane expansion; this covers in
particular its integer-real-part case. Every real argument
uses its period chart.
Multiplication of these exact factorizations gives
\[
 \begin{split}
 \mu_N
   &=N^{-3/2}
       \exp\left\{N\sum_j\nu_jJ_j(\ell_j)
            +\sum_j\nu_j(a_j+\tfrac12)J_j'(\ell_j)\right\}
         \mathfrak W_N\,\mathfrak U_N,\\
 \mathfrak W_N
   &=\prod_{j\ {\rm period\ chart}}
        \bigl(1-e^{\tau_j2\pi i(N\ell_j+a_j)}\bigr)^{\nu_jk_j},
 \qquad
 \mathfrak U_N=1+O_{\rm hol}(N^{-1}).
 \end{split}
 \tag{17}
\]
Here each \(J_j\) has the specified half-plane or chamber mark.
The exact nonzero holomorphic unit \(\mathfrak U_N\) is the
product of the exact normalized remainder factors; no equality
is asserted with a truncated series. For a crossing, the same
formula has \(N^{-1/2}\), its three arguments, and the full
prefactor (16).

This is a local normal form for the same meromorphic gate,
including all its divisors. It is not a rectangular extension
of its finite support. The existing factorial-divisor criterion
shows that distinct affine zero hyperplanes need not cancel
pole hyperplanes in (13). They remain present in (17).

## 4. Joint Fourier factors in a pointed cone

Let \(\mathbf z\in\mathbb C^d\) be independent retained label
coordinates, and let the wrapped arguments be real affine
forms
\[
                  \ell_j(\mathbf z)=\mathbf a_j\cdot
                         \mathbf z+b_j,\qquad
                  \mathbf a_j\in\mathbb Z^d\setminus\{0\},
                  \quad b_j\in\mathbb R.
 \tag{18}
\]
The actual gate forms (14), and their original integer
complementary identifications, have this form. Write
\(h=\Im\mathbf z_*\) at the chart center. Choose a real \(v\)
with \(\mathbf a_j\cdot v\ne0\) for every form that is real
there. For sufficiently small fixed \(\varepsilon>0\), the vector
\(v_*=h+\varepsilon v\) has nonzero pairing with every
\(\mathbf a_j\), and those pairings preserve the signs of
all nonreal arguments. Set
\[
         \tau_j=\operatorname{sgn}(\mathbf a_j\cdot v_*),
         \qquad e_j=\nu_jk_j.
 \tag{19}
\]
Thus the choice keeps every nonreal canonical half-plane branch
and chooses a coherent side at the real arguments. Along
\(\mathbf z=\mathbf z_*+itv_*\), \(t>0\) fixed and small,
every exponential in (17) has modulus less than one for all
sufficiently large \(N\), also with the actual bounded offsets.
If all arguments are real at the center, \(h\) is orthogonal
to all their gradients and this reduces to a generic imaginary
direction.

**Theorem 2.** Expand every factor of
\[
 \mathfrak W_N(\mathbf z)
       =\prod_j
          (1-e^{\tau_j2\pi i(N\ell_j(\mathbf z)+a_j)})^{e_j}
 \tag{20}
\]
in its convergent binomial series on this common side.
The expansion is locally normally convergent there. Its Fourier
frequencies, in the variables \(e^{2\pi iNz_\alpha}\), lie in
\[
 \mathcal C=\left\{\sum_jr_j\tau_j\mathbf a_j:
                                      r_j\in\mathbb Z_{\ge0}\right\}.
 \tag{21}
\]
Every nonzero term has strictly positive pairing with \(v_*\).
The coefficient of frequency zero is exactly \(1\), for all
levels and all actual offsets; this coefficient identity is
algebraic, whereas convergence on the specified local chart
holds for sufficiently large \(N\) as above. This includes negative \(e_j\)
and arbitrary linear dependencies between the affine forms.

**Proof.** For integer \(e\), the series
\((1-u)^e=\sum_{r\ge0}(-1)^r\binom er u^r\)
is finite if \(e\ge0\) and absolutely convergent for \(|u|<1\)
if \(e<0\). Its constant term is one. Each nonconstant choice
contributes a frequency \(r\tau_j\mathbf a_j\), whose pairing
with \(v_*\) is \(r|\mathbf a_j\cdot v_*|>0\).
Thus no nonzero tuple of choices can have total frequency zero.
The tuple of all zero choices gives coefficient one.

The finite product converges normally on smaller regions where
all \(|u_j|<1\) uniformly. Frequency grouping is unambiguous:
if \(\delta=\min_j|\mathbf a_j\cdot v_*|>0\), a fixed frequency
\(\lambda\) can arise only from tuples with
\(\sum_jr_j\le\lambda\cdot v_*/\delta\). There are finitely many
such tuples. Affine constants and literal offsets change their
scalar coefficients, not their frequencies or this argument.
\(\square\)

All seven forms in (14), and all three crossing forms, are
nonconstant in the retained labels of the actual gate, so the
theorem applies directly to each gate and to any collection
before imposing further identifications. It also applies after
actual affine wire identifications whenever the wrapped forms
remain nonconstant and have real affine constants in the remaining
coordinates: choose the pointing vector in that coordinate space.
Any form that becomes constant instead
is retained as its explicit scalar factor in (20); its zero
cannot be excluded by this Fourier argument. In particular an
exterior parameter is not silently varied to make such a form
nonconstant. With fixed complex affine constants, the same cone
proof applies if a common pointing vector for the prescribed
signs exists; its existence is not inferred from \(h\) in that
case.

Theorem 2 concerns \(\mathfrak W_N\), not the Fourier expansion
of the complete action, normalized remainder, or lattice kernel.
It proves that the wall-transition factors do not cancel their
specified zero-frequency sector. It does not say that all their
other coefficients are nonzero.

## 5. Positive prefixes and the retained geometric mark

The original positive-prefix theorem proves that all seven
arguments of every proper multiplication gate and all three
arguments of a signed crossing have nonzero sines at its
specified positive primitive point. The construction leaves
one incident factor for the final complementary pairing; it
does not treat that final pairing as a strict multiplication
gate.

Consequently every gate in that algebraically regular resolution
has a local factorial description (17): use a half-plane chart
at a nonreal argument and a real-chamber chart otherwise.
This fills the local analytic description without assuming that
all arguments have real part between zero and one. It retains
every \(N\)-dependent Fourier factor and does not assert a
nonzero unfactored symbol at a real out-of-support argument.
The exact complementary pairing and its \(N-1\) reversal stay
unchanged.

A geometric primitive already marked by continuation must also
stay unchanged. Here is the branch bookkeeping explicitly.
For a single argument, two continued primitives with the same
original normalization can differ locally by
\[
                  2\pi i(w\xi-h),\qquad w,h\in\mathbb Z.
 \tag{22}
\]
Indeed continuation of \(\log(2\sin\pi\xi)\) around its simple
zero at an integer \(r\) adds \(2\pi i\); its primitive changes
by \(2\pi i(\xi-r)\). Composing finitely many signed loops
gives (22). A change of derivative branch also changes the
offset prefactor by the exact constant
\(\exp\{2\pi i(a+\tfrac12)w\}\).

For several arguments, if the previously marked phase is
\[
              S_{\rm geom}(\mathbf z)
                =S_{\rm chamber}(\mathbf z)
                         +2\pi i(\lambda\cdot\mathbf z+\gamma),
 \tag{23}
\]
retain that character and its associated offset constants.
This includes any Fourier character already present in the
spectral--Newton adapter, such as its signed-crossing shift
\(-2\pi i\sigma x\); it is not restricted to new factorial
monodromy.
Relative to \(e^{NS_{\rm geom}}\), the Fourier factor in
(17) is multiplied by
\(e^{-2\pi iN(\lambda\cdot\mathbf z+\gamma)}\).
Thus the wall-factor coefficient associated to this geometric mark
comes from its coefficient at frequency \(\lambda\), not
automatically from frequency zero. Theorem 2 identifies it
with the nonzero constant coefficient only when the character
has the corresponding zero frequency; it does not remove a
nonzero \(\lambda\).

Even when that local branch agrees, the original finite support
cycle, the other Fourier modes, endpoints, shared-wire
contractions and first-normal closing terms remain. No
intersection number or full geometric contribution is deduced
from the factorial chamber or its unit remainder.

## Direct sources

* [Exact factorial interpolation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/exact_factorial_interpolation_and_complex_contours.md),
  SHA256
  \(\texttt{1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72}\):
  the specified gamma product, reflection, strip asymptotics with
  complex offsets and the actual supported residue cycle.
* [Uniform half-plane continuation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_factorial_uniform_halfplane_continuation.md),
  SHA256
  \(\texttt{0514ffe3e13a887eccd9099b306117ee86553f0731d976315e2607b3e33493fa}\):
  marked \(J_\pm\), arbitrary off-real compact charts and the exact
  one-period phase.
* [Factorial divisor criterion](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_factorial_rectangle_divisor_criterion.md),
  SHA256
  \(\texttt{462b8c22c73f73b12152bca96cf6636708dcf153c2cbc2751458454827b3ddf8}\):
  actual zero/pole orders and the limitation of joint rectangular
  extension for multiplication.
* [Spectral--Newton adapters](research_newton_spectral_legendre_adapters.md),
  SHA256
  \(\texttt{34c0e2e1114488c6ac82a5dffbdbd8a4a8d85e7fbba252de91833dc8d697e303}\):
  literal multiplication and signed-crossing coefficients, carrier,
  transpose, offsets and the retained local Fourier lift.
* [Positive primitive prefixes](research_positive_primitive_prefix_regularity.md),
  SHA256
  \(\texttt{a01b55a71d133aadff4aac0929e50de03e1059991d6874e81646c770eb5604a6}\):
  all gate sine exclusions for the stated proper-prefix resolution,
  without a prior factorial-chart or cycle conclusion.

The arguments use written proofs and source-text reads only. No
mathematical code, numerical evidence, tests or compilation are used.
