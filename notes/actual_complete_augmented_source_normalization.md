# Complete augmented-link source normalization: no hidden exponential factor

29 October 2026. At the ORIGINAL boundary-parabolic complete color,
the marked raw augmented-link period differs from its reduced
zero-framed quantum/Kashaev evaluation only by a unit phase. The
full one-cut ADO modified evaluation has the additional EXACT factor
i^(N+3)/N. This is not an assertion about a generic meridian germ's
size. It follows by retaining and then specializing that whole
normalization germ and all actual turns.

## 1. Which scalar is raw, reduced, or modified

Fix N>=2, d=N-1, q=exp(pi i/N), Q=q^2, x=q^d and
kappa=q^(d^2/2). The raw source here is the one in the
[literal augmented pretzel diagram](actual_odd_pretzel_augmented_transfer_source.md):
every full physical crossing has its original common Cartan,
the crossing circles are the exact auxiliary pivotal traces L_N,
and the main component has k genuine cups, k-1 ordinary caps and
ONE original marked cap. Their balanced entries are

    p_ab=Nx^(-b)delta_(a+b,d),
    ell_ab=x^a delta_(a+b,d)/N, m_ab=x^b/N^2.

The [direct turn/source calculation](quantum_bridge_cap_source.md)
proves that these are precisely the original left/right duality
and the selected cut projector. Specifically, with g=K^(1-N),
e=psi phi, psi_a=1,phi_a=1/N and D=g^(-1)e,

\[
 \operatorname{Tr}(gDC)=\operatorname{Tr}(eC),\qquad
 m p=1.                                                  \tag{1}
\]

Each cup contributes its actual N, each ordinary cap 1/N, and
the single marked cap 1/N^2. Their net scalar is EXACTLY 1/N,
the original cut average. There is no other cut normalization
waiting outside this raw tensor contraction. Balanced factorial
changes cancel by exact basis covariance on every internal wire;
their potentially exponential condition numbers are never estimated
as an external scalar.

At completeness the original twist is

\[
 \theta_d=q^{(d^2+2(1-N)d)/2}=q^{-d^2/2}=\kappa^{-1}.
                                                               \tag{2}
\]

Therefore any recorded change from the actual diagram's framing
to the chosen component framings is a product of integer powers
of theta_d, and has modulus one. For a braid normalization using
total writhe w it is theta_d^(-w)=kappa^w. If individual component
self-framings are prescribed instead, their difference from this
convention is a linking/framing character, again a unit phase.
Mutual crossings are not silently called self-writhe; only the
modulus statement is independent of that convention.

Let A_raw be the actual tensor scalar and F_red the reduced
zero-framed evaluation with the same chosen marked component.
With its explicitly recorded framing character zeta_(N,L),

\[
 F_{\mathrm{red}}(L)=\zeta_{N,L}A_{\mathrm{raw}}(L),
                    \qquad |\zeta_{N,L}|=1.             \tag{3}
\]

This applies to the original auxiliary-circle diagram before or
after its exact finite L_N contraction. Each closed auxiliary circle
uses an ORDINARY pivotal trace already in L_N, with no added1/N,
no division by its zero quantum dimension, and no extra modified
dimension attached to it. Modifying every component independently
would define a different normalization from the original one-cut
source.

## 2. The modified dimension is specialized as a WHOLE germ

At fixed root q, use the original meridian M=-q q^alpha=e^u,
so alpha=d+u/Log q. The given modified dimension is

\[
 d_N(\alpha)=-q^{N(1-N)/2}
  \frac{q^{\alpha+1}-q^{-\alpha-1}}
       {q^{N\alpha}-q^{-N\alpha}}.
\]

Substitution, retaining both numerator and denominator, gives the
ENTIRE specified local meridian function

\[
 d_N(e^u)=i^{N+3}\frac{\sinh u}{\sinh(Nu)},\qquad
 \boxed{d_N(1)=\frac{i^{N+3}}N.}                         \tag{4}
\]

This is a removable value, not a cancellation of two separately
evaluated zeros. The full one-cut modified invariant, by its
original definition, is d_N(M) times the reduced selected tangle
scalar. Consequently

\[
 \mathcal N_N(L;M=1)=\frac{i^{N+3}}N F_{\mathrm{red}}(L),
 \qquad
 |\mathcal N_N|=\frac1N|A_{\mathrm{raw}}|.               \tag{5}
\]

There is ONE such factor, on the marked component. The other
components were closed by the ordinary trace in section 1. No
claim about q-transverse derivatives is made: (4) is the actual
meridian germ at a fixed root, not a substitution of a generic-q
ordinary pivot for the full modified source.

Equations (3)--(5) prove, in the respective two normalizations,

    |chi_red|=1, |chi_full|=N^(-1),
    (1/N)log|chi_red|=(1/N)log|chi_full|+log(N)/N=0.

In particular the previously unspecified common external chi_N
has zero exponential rate at THIS complete pointing. It need
not have polynomial size on an arbitrary moving peripheral germ.

## 3. The enhanced Kashaev comparison extends to a link

The original comparison note states its conclusion for knots.
The local matrix identities used there also suffice for the
present multicomponent source; no quotient-color argument is needed.
Here is the missing connectivity check.

Let a b-strand braid be colored by the full original V_N and
close every head but the chosen first one with the actual pivot.
The resulting cut matrix C commutes with E,F,K. This follows by
partial trace of the explicit Hopf coproduct identities. For the
K-pivot convention, tracing [A,E_prefix K_last+E_last] ordinarily
over the last head yields commutation with E_prefix. For F, use
K conservation and cyclicity to obtain

    Tr_last K_last[A,K_prefix^(-1)F_last]=0.

Multiplying the original pivot by its complete scalar sign leaves
this intertwining assertion intact. Repeating the argument closes
all other heads, regardless of how many link components their
permutation has. On the remaining V_N, K has N distinct weights
and all internal F coefficients are nonzero. Thus C is a SCALAR
matrix, at all even and composite N as well. Connectivity of the
closed link was not used. The selected Tr(eC) is that scalar.

The exact original Fourier/diagonal comparison in
[the crossing calculation](kashaev_crossing_and_period_lattice.md)
therefore works unchanged on this link cut. The large factorial
similarities on traced factors cancel by cyclicity; the one on
the open factor cancels because C is scalar. The local equality
gamma alpha_q=alpha_K cancels all writhe factors. This compares
the enhanced Kashaev period with the ordinary quantum-group
enhancement with unknot value1, without any exponential gauge.

To fix the dual/primal convention explicitly, the crossing note
uses the dual pivot K^(-1). The original matrix

    B v_j=(-1)^j q^(j(j-N)) v_(d-j)

in [the complete pointing comparison, section 2](kashaev_ado_pointing.md#2-exact-specialization-to-the-original-kashaev-period)
intertwines that dual module with the primal one, conjugates its
pivot to K, and satisfies R^T=(B tensor B)R(B^(-1) tensor B^(-1)).
Those are direct generator and finite-crossing identities. The
same full cut scalarity cancels this open-factor conjugation as
well. Thus the primal K in the next display and the dual K^(-1)
in the enhanced crossing comparison refer to identical scalar
evaluations, with no additional normalization character.

There is one useful sign when the latter is instead expressed
with the ADO pivot/twist. At completeness

    g_ADO=(-1)^d K, theta_ADO=(-1)^d alpha_q.

For a b-strand closure of total writhe w, the trace and framing
ratios multiply to (-1)^(d(b-1-w)). If that closure has c components,
its permutation gives w congruent to b-c modulo2. Hence

\[
 F_{\mathrm{red}}^{\mathrm{ADO}}(L)
     =(-1)^{d(c-1)}\langle L\rangle_N                  \tag{6}
\]

in those two explicitly specified enhanced-framing conventions.
Other recorded choices of individual zero framings add only their
already described unit twist character. In particular

\[
 \boxed{|\langle L\rangle_N|=|F_{\mathrm{red}}(L)|
                                  =|A_{\mathrm{raw}}(L)|.} \tag{7}
\]

For the odd-pretzel complete augmented diagram there is one main
component and s genuine auxiliary circles, so c=s+1. The sign in
(6) is (-1)^(ds); it is immaterial to the exponential rate but is
not asserted to be one. The local full Cartan and the exact
half-twist phases remain IN A_raw and in its proved leading
constant. They are not counted a second time in chi.

## 4. What this closes, and its precise limit

For the ORIGINAL one-cut enhanced Kashaev link evaluation, the
full raw-period asymptotic has EXACTLY the same absolute value
and exponential rate. For the full modified ADO evaluation it
has the factor1/N and the phase in (4); its leading N-power must
be adjusted accordingly. This closes the external normalization
gate at the complete augmented source. It does not identify its
action with a manifold volume without the geometric face-gluing
calibration, and it proves no Dehn-filling or fixed-knot statement.

The [audit](../experiments/audit_actual_complete_augmented_source_normalization.py)
compares original enhanced Kashaev matrices, ordinary quantum
matrices, and the actual ADO pivot/twist through full cuts of
both knots AND multicomponent links. It checks scalarity, the
component-dependent sign, and the entire modified-dimension germ.
It does not replace a link by a knot on the basis of an invariant.
