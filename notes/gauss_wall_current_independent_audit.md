# Independent audit of the Gauss-wall finite current map

27 October 2026. Both
[the actual wall/cut-current theorem](actual_gauss_wall_cut_current_complex.md)
and [the elevated-source restrictions](degree_elevated_wall_source_and_divided_ward.md)
pass after the explicit raw-to-matrix factor \(N\) is retained.
This audit checks their finite identities and scope; it supplies
no internal Gaussian source comparison.

## 1. Residue, anchored primitives and the source class

With \(F=1-\eta v\), direct substitution
\(d\log\eta=-dF/(1-F)-d\log v\) gives
\[
 \operatorname{Res}_{F=0}
   \left(-\frac{d\eta}{\eta}\wedge\frac{\Omega_0}{F}\right)
      =\Omega_0=-dT\wedge d\log v .
\]
Thus both stated primitive signs are correct.
The beta integral is
\[
 \binom{N-1}{j}\int_0^1t^j(1-t)^{N-1-j}dt=1/N .
\]
Their difference has coefficients \(C_{ij}v^{i-j}/N\).
Every off-diagonal coefficient is exact on \(\mathbb C^*\),
leaving precisely \((\operatorname{Tr}C/N)[d\log v]\).
For the actual unweighted cut \(C=F_N(Y)I\), the class is
\(F_N(Y)[d\log v]\), nonzero as a family by its ordinary anchor.
This does not assert nonvanishing of every complete value.

Angular integration at \(T=1/2\) kills off-diagonal terms.
The two incomplete-beta rows have total weights \(1/2\),
and reversal gives \(w_{N,N-1-j}=1/N-w_{N,j}\).
Hence the actual meridian Weyl matrix interchanges them,
while every diagonal Gamma/frame conjugation preserves each.
All normalization statements refer to the paired source lattices
at a singular meridian.

## 2. Finite endpoints and the original \(1/N\)

For a zero-extended array \(J\), the coefficient at an interior
index in the backward difference of the positive head weights
is \(\binom Nj/(N2^N)\). At zero the extra coefficient is
\(-1/N\); at \(N\) the binomial endpoint remains. Therefore
\[
 \lambda^+_{\rm head}((S-1)J)=B_N(J)-J_0/N,\qquad
 \lambda^-_{\rm head}((S-1)J)=-B_N(J)+J_N/N .
\]
The negative and positive tails in the relative extensions
supply \(+J_0/N\) and \(-J_N/N\), respectively.
Their sum is exactly the ordinary normalized full-index sum.
The \(j=N\) entry in \(B_N\) cannot be dropped.

The original Green arrays already include \(1/N\). The current
note correctly sets \(I_{\rm mat}=NI_{\rm raw}\) and
\(J_{\rm mat}=NJ_{\rm raw}\) before applying matrix-normalized
rows. In raw coordinates the rows are \(N\lambda^\pm\),
the wall row is \(NB_N\), and the endpoint terms are
\(J_{{\rm raw},0}\), \(J_{{\rm raw},N}\).
This is an exact conversion, not an absorbed endpoint constant.

The conclusion \(B_N(J_{\rm cut})=0\) is justified for the stated
UNWEIGHTED original cut: each hemisphere is \(F_N/2\), its
actual scalar annihilator kills this, and all other zero-extended
flow differences sum to zero. The proof does not extend scalar
cut behavior to an arbitrary coupled word. Unsummed currents
and their moment factors remain present before those sums.

## 3. The elevated source restrictions are exact

The degree-\(N\) source pairing is the literal primitive tensor
construction on the already proved two-dimensional source.
Its row has binomial multiplicities and gives the desired
\(B_N\) with the stated extra factor \(1/N\), not \(1/(N+1)\).
It does not prove compatibility with the true divided Hopf
coproduct and its mixed terms.

On \(\operatorname{End}(V_N^{\otimes b})\), integer matrix
weights lie between \(-b(N-1)\) and \(b(N-1)\).
The finite-head divided E-adjoint lowers that weight by \(N\).
Hence its \(2b\)-th power is zero, whereas the primitive
\(\operatorname{Sym}^N\) action has nonzero \(e^{2b}\) for
\(N\ge2b\). Irreducibility in characteristic zero proves
the claimed obstruction to any nonzero full-SL2 intertwiner
into this space or a subquotient with the same bound.
It leaves the stated Borel, tail and non-equivariant routes open.

Cancellation of \(1-Q^N\) in the quantum binomial gives exactly
\[
 d_{N,j}=\frac{(-1)^{j-1}Q^{-j(j-1)/2}}{1-Q^j}.
\]
Thus the trial diagonal adapter has middle magnitude
\(2\binom Nj\sin(\pi j/N)\) and endpoint magnitude one.
The central binomial coefficient and sine bounds prove
both displayed exponential condition-number lower bounds.
This conclusion is relative to the explicitly specified trial
identification of endpoint and middle normal degrees.

The literal level-two stabilized crossing has cut entries
\(1\) and \(2w-1\), including its original pivot and twist.
Its normalized transfer polynomial is \(w\); after a scalar
knot cut it is \(Fw\). The auxiliary transfer source is then
\(\operatorname{diag}(0,2F)\), giving hemisphere values
\(F/4,3F/4\), as stated. This directly prevents identifying
a second transfer reflection with the actual cut Weyl action.

These statements specify real finite co-sources and current
constraints. They neither identify their Gaussian images nor
show that the selected geometric contribution survives.

## 4. The centralizer normal-moment refinement also passes

The subsequent
[normal residue/current theorem](centralizer_normal_residue_and_actual_cut_moments.md)
has been checked independently in its current form.
Expansion of \(1/(1-\eta v)\) gives
\(\operatorname{Res}_E(b_N^h\nu_{\rm cut})=-(-T)^h\Omega\).
The south representative must be \(P(b_S-1)\).
Its difference from the north polynomial is divisible by the
Gauss-wall factor; the stated \(\Xi_h\) integrates its remaining
normal powers exactly, with no logarithmic E residue.

Contraction by \(V_b=-\eta\partial_a\) gives
\(P(b)d\eta\wedge dv/F\). The two current residues are exactly
\([P(-T)-P(0)]d\log v\) and
\([P(-T)-P(-1)]d\log v\).
Their difference is the retained endpoint class
\([P(0)-P(-1)]d\log v\).
With a nonconstant source kernel the product correction is
essential:
\[
 d\,\iota_{V_b}(P f_C\nu_{\rm cut})
              =(P'f_C-XP\partial_Tf_C)\nu_{\rm cut}.
\]
Its residue equals minus the differential of the current
residue, as required when \(d\eta/\eta\) is written first.
The Bernstein integration-by-parts identity (17), including
both endpoints and its dimension-\(N-1\) target, is correct.

The correct paired co-source uses rising-factorial Toeplitz
moments; the falling-factorial symbol map cannot replace it
against a general kernel. The
[exact dual clock theorem](dual_clock_normal_cut_source.md)
now extends this to the whole cut clock and to bounded
normalized cut-position moments with pole order independent N.
This is the normalized TRACE extension. Its agreement with
the original average cut holds for the actual conserving
diagonal arrays, not arbitrary off-diagonal Ward matrices.

The raw normalized b-moments remain uniform interval moments
\((-1)^h/(h+1)\) and have Hankel matrices of unbounded rank.
This prevents a shortcut to a finite critical algebra in the
FRAMING variable; it does not obstruct a finite isolated
TRANSVERSE critical algebra after the required framing pushforward.
The internal-transfer/second-framing and Gaussian-source maps
remain additional constructions.

