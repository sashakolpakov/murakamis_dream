# The actual first normal high-color crossing has Frobenius degree at most two

Research proof and exact audit, 27 October 2026. The first
\(\delta=1-Q^N\) coefficient of the actual integral high-color
crossing is a quadratic operator on the classical Frobenius
multiplicity variables, with arbitrary finite head coefficients.
The first resonant tail has a universal exact factorization.
Both statements retain the full Cartan and mixed block signs.

This is an actual first-normal crossing theorem. It does not identify
whole low/high color jets or construct the full two-current Gaussian
source map.

The normal variable differentiates the original generic integral
matrix family with its ordinary pivotal data. A frozen root ADO
pivot is a different off-root source and requires its explicit
route adapter; no scalarity of that frozen family is assumed.

## 1. Actual matrices and the filtration being used

Use [the high integral color](high_integral_color_frobenius_wall_source.md),
with dimension \(N(r+1)\), \(m=N(r+1)-1\), and the constant sign
basis \(w_{a,s}\), \(0\le a\le r\), \(0\le s<N\).
At the root the ordinary head matrices are independent of a.
The divided matrices are
\[
 \mathsf E=[E^N/[N]_q!]_{q_N}=\tau e_{\rm cl},\qquad
 \mathsf F=[F^N/[N]_q!]_{q_N}=f_{\rm cl},
 \qquad \tau=(-1)^{Nr-1}.
\]
The root block number is \(a=(r-h_{\rm cl})/2\), so multiplication
by a is a degree-one classical enveloping operator.

Give \(e_{\rm cl},f_{\rm cl},h_{\rm cl}\) PBW degree one.
On two strands use total degree for
\(U(\mathfrak{sl}_2\oplus\mathfrak{sl}_2)\).
Head matrix coefficients have degree zero. The full root crossing
also has its literal block flip and parity
\(\varepsilon^{a+b}\), \(\varepsilon=(-1)^m\); these are retained
separately, not asserted to be bounded-degree polynomials in a,b.

Write \(R(\delta)=R_0+\delta R_1+O(\delta^2)\).
Then
\[
       R_0^{-1}R_1\in
       U_{\le2}(\mathfrak{sl}_2\oplus\mathfrak{sl}_2)
                            \otimes\operatorname{End}(\text{heads}). \tag{1}
\]
This assertion is uniform in N and r. Its scalar coefficients may
depend on N,r and the marked root. It is not a uniform numerical
norm bound on those coefficients.

## 2. Transfer orders and the universal resonant factor

The full positive un-checked R is
\[
 q^{H\otimes H/2}
   \sum_{k\ge0}q^{k(k-1)/2}\rho^k[k]_q!\,
                         E^{(k)}\otimes F^{(k)},
 \qquad E^{(k)}=E^k/[k]_q!,\quad \rho=q-q^{-1}.          \tag{2}
\]
Each divided matrix has regular integral Gaussian entries.
The factor \([k]_q!\) has \(\delta\)-order
\(\lfloor k/N\rfloor\), since every positive multiple of N
contributes one simple zero. Hence all \(k\ge2N\) transfers
vanish modulo \(\delta^2\).

For \(k=N+b\), \(0\le b<N\), divided-power multiplication gives
\[
 D_{N+b}=
 \frac{q^{N(N-1)/2+Nb}\rho^N[N]_q!}
             {{N+b\brack b}_q}\,
 D_b\,(E^{(N)}\otimes F^{(N)}),                       \tag{3}
\]
where \(D_k\) denotes the k-th term of the nilpotent sum in (2).
This is an exact generic identity before taking a normal coefficient.

At the root,
\[
 {N+b\brack b}_{q_N}=(-1)^b,\qquad q_N^{Nb}=(-1)^b,
\]
so these factors cancel. Also
\[
 \left[
   q^{N(N-1)/2}\rho^N[N]_q!/\delta
 \right]_{q_N}
      =N(-1)^{N-1}=:\kappa_N .                         \tag{4}
\]
Indeed \(\rho^N[N]_q!=
(-1)^Nq^{-N(N+1)/2}(Q;Q)_N\), and
\((Q;Q)_{N-1}=N\). Therefore the entire first resonant tail is
\[
 [R_{\ge N}/\delta]_{q_N}
       =\kappa_N R_0(\mathsf E\otimes\mathsf F).        \tag{5}
\]
Equation (5) includes checked crossings as written: the divided
operator is on the INPUT, to the right. The same full root R,
including the mixed parity and original common half-Cartan line,
must be used. Moving an isolated factor through it without its
sign would change this statement.

The Frobenius degree of (5) is two.

## 3. Nonresonant head terms have degree at most one

Fix \(k<N\). In \(E^k\) or \(F^k\) at most one head boundary
can be crossed. If neither side crosses, every factor is
\([AN+s]_q\), \(s\not\equiv0\bmod N\). With
\(\delta=1-q^{2N}\), its first derivative at the root is,
apart from the root sign \((-1)^A\), affine in A:
\[
 \left.\partial_\delta[AN+s]_q\right|_0
  =-\frac{(-1)^A}{2N}
    \left[
     \frac{(AN+s)(q_N^s+q_N^{-s})}{\rho_N}
       -[s]_{q_N}\frac{q_N+q_N^{-1}}{\rho_N}
    \right].                                         \tag{6}
\]
The constant beta gauge cancels every block-dependent root sign
in the ordinary head coefficient. Differentiating a product once
therefore gives a degree-one polynomial in the two block numbers.

If E crosses one boundary, its one vanishing integer has first
normal value proportional to \(r-a+1\). The other head factors
are nonzero. In the beta gauge its remaining sign is independent
of a: for input head s<k the total sign is
\((-1)^{kr+1+s}\). Thus this contribution is an actual
\(e_{\rm cl}\) factor with a head coefficient. The F boundary
likewise gives \(b+1\), hence \(f_{\rm cl}\), with no remaining
block-dependent sign. If both sides cross, their two zeros
give order \(\delta^2\), so nothing survives in the first normal.

The remaining factors \(\rho^k\), \(q^{k(k-1)/2}\), and
\([k]_q!^{-1}\) are regular head-dependent scalars for \(k<N\).
They do not raise the Frobenius degree. Hence the entire
nonresonant nilpotent first-normal coefficient has degree at
most one after the retained root parity is factored.

## 4. The Cartan part raises the bound to two

The unrolled weight is
\(H_{a,s}=m-2s-2Na\).
Since \(q=q_N(1-\delta)^{1/(2N)}\),
\[
 \left.\partial_\delta q^{H_1H_2/2}\right|_0
                    =-\frac{H_1H_2}{4N}
                                  q_N^{H_1H_2/2}.      \tag{7}
\]
The multiplier is quadratic in a,b. Its product with a
first-normal boundary or resonant term is second order and
does not enter R_1. Equations (5)--(7) prove that, after factoring
the root signed block swap, every head matrix coefficient of
R_1 has total Frobenius degree at most two.

The root crossing is a signed block flip tensored with the
original head crossing. Conjugation by it preserves the PBW
degree: the flip permutes the two Lie algebras, parity changes
the signs of e,f and leaves h fixed, and the head factor only
changes head coefficients. This proves the interaction form (1).

For a negative crossing, differentiation of the exact inverse gives
\[
 (R^{-1})_1=-R_0^{-1}R_1R_0^{-1}.
\]
The same root conjugation argument proves the identical
degree bound. The root half-Cartan and zero-framing factors are
never replaced by their ideal numerical values.

A coherent realization of the classical multiplicity variables
turns (1) into a differential operator of order at most two,
with its one-sided source/dual connection terms retained.
It does not make the entire divided Hopf action primitive or
remove its mixed coproduct terms.

## 5. The same bound holds for every braid word and its knot closure

This local filtration is stable under arbitrary word composition.
Let W(delta) be any fixed braid word on b high-colored strands.
The derivative of a product, written in its interaction frame,
is a sum of conjugates of the local interactions R_0^(-1)R_1.
Every root factor is its head crossing times a signed permutation
of the Frobenius factors. These permutations exchange generators
and their parity factors change only the signs of e,f. Therefore

    W_0^(-1)W_1 lies in
       U_(<=2)(sl2^b) tensor End(all heads).             (8)

There is no crossing-count or bridge-count restriction on (8).
Its coefficients and number of terms may depend on the word;
the enveloping DEGREE stays at most two. A root pivot has no
block dependence, and its first normal coefficient is affine
in the unrolled weight, hence of degree at most one. The
original zero-framing twist is a scalar on each generic integral
color and introduces no extra Frobenius degree.

Now close all but one strand of a braid whose closure is one
knot. For the scalar Ward corollary below, use the ACTUAL generic
ordinary integral ribbon family, with pivot K(q) and its matching
zero-framing twist. Its reduced scalar is C_n(q). The root
comparison with the ADO pivot was proved with its explicit signs;
it is not an equality of those pivotal families off the root.
The root Frobenius permutation has one cycle. In its
partial trace, the Frobenius factors of any inserted monomial
are multiplied in their order along that component. Degrees
add to at most two. Transporting them past parity operators
changes only their recorded signs. The total parity around
the uninserted component is even, as in the high-color closure
proof. Consequently the first normal long-knot matrix has

    C_1 in End(head) tensor U_(<=2)(sl2),                (9)

with the actual pivots, twist and ordered insertions retained.
This is a statement about the full matrix before choosing a
new source or identifying an internal geometric frame.

There are exact resulting Ward identities. The generic actual
integral-color long-knot operator is C_n(q) times identity, so
its first normal coefficient (9) is also scalar. For r>=2 the
image of U_(<=2)(sl2) under the adjoint classical action is the
sum of spins zero, one and two, of dimensions 1,3,5. This follows
directly by the highest vectors 1,e,e^2 and repeated commutation
with f; their distinct h-weights and the nonzero raising strings
make the three summands independent. The quadratic Casimir
only changes the scalar summand in the given representation.
Thus all eight nonscalar spin-one and spin-two coefficients of
(9) vanish as head matrices. Its scalar head coefficient is
the actual derivative of C_n(q) times the head identity.

These are finite exact source identities for an arbitrary knot,
and their coherent differential realization is given by the
[actual two-flag Ward dictionary](high_color_two_clock_normal_source.md).
They do not by themselves identify the relevant geometric
current or prove that a selected geometric period survives.

If one instead freezes the auxiliary ADO pivot to K(q)^(1-N)
off the root, the matrix-degree bound (9) still holds: its normal
pivot contribution is still degree one. Its generic long matrix
need not be scalar, however. The eight vanishing coefficients
then require the exact pivotal/normal source adapter and do not
follow from root-only pivotal equality. This qualification is
essential to the final Ward corollary, not to (1), (5), or (8).

## 6. Independent exact tests

[The audit](../experiments/audit_high_color_first_normal_r_degree.py)
assembles the ACTUAL integral R entries over a finite field and
its dual numbers, using polynomial Gaussian recursion before
specialization. A primitive fourth-level root retains the full
half-Cartan phase. Its dual parameter is exactly
\(q=q_N(1-\delta/(2N))\).

At \((N,r)=(2,3),(3,3),(4,4),(5,3)\), it checks:

* all transfers \(k\ge2N\) vanish to first order;
* 3112 resonant coefficient identities (5), including boundaries;
* all 174 nonzero head blocks of the parity-stripped first normal
  lie in the exact PBW-degree-two span;
* some blocks do not lie in degree one, so the quadratic bound
  is genuinely needed in these examples.

The PBW span is computed independently from the classical
e,f,h matrices, with modular pivot rows and exact reconstruction;
no proposed coefficient decomposition is supplied to the test.
[Results](../experiments/high_color_first_normal_r_degree_results.json)
record the ranks and level data. These checks support the uniform
proof; they are not a selected-period or global-current theorem.

The [actual-source audit](high_color_wall_source_independent_audit.md)
checks the high integral matrix, divided source and Ward
dictionary used here. The [memory-clock proof](actual_memory_clock_and_normal_transfer.md)
then applies this crossing bound with its exact first-normal
carry factors and independently checked inverse crossing.

