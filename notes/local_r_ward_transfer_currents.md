# Literal crossing-transfer Ward currents and their partial pushforward

Research construction, 27 October 2026. This writes the actual R
intertwining identities coefficient by coefficient in the unwrapped
transfer index. They give exact divergence currents and an explicit
rank-one cyclic-edge source. The current identities compose under
the actual tensor contractions and have a linear formal Gaussian
pushforward with all inserted moments retained.

No map from the scalar partially summed Gaussian block to the full
matrix Ward complex is assumed here. A nonzero local cyclic-edge
source is not asserted to be a nonzero selected framing cohomology
class or global geometric contribution.

## 1. Actual coefficients and conventions

Fix N>=2, q=exp(pi*i/N), Q=q^2. Allow two colors x_1,x_2, with
M_i=-q x_i. In the balanced basis the generator entries are

    K_i(n)=x_i Q^(-n),
    f(n)=1-Q^(n+1),       0<=n<N-1,
    e_i(n)=M_i Q^(-n)-M_i^(-1), 1<=n<N.

Outside the displayed ranges f and e_i denote zero actual matrix
edges. In particular e_i(0)=0. The last absent cyclic raising edge
would instead have coefficient kappa_i=M_i-M_i^(-1).

Let s=+1 or -1 and let r_s(a,b,k) be the actual checked crossing
coefficient from inputs (a,b) to outputs

    (c,d)=(b+s k,a-s k),                         (1.1)

with the output colors x_2,x_1. Extend it by zero unless a,b are
in 0,...,N-1 and

    s=+1: 0<=k<=min(a,N-1-b),
    s=-1: 0<=k<=min(b,N-1-a).

The explicit balanced formulas are those proved from the literal
R matrices in [the actual four-plat calculation](figure_eight_whole_source_identity.md),
Section 2. Their common full Cartan line is retained. Every Ward
identity here is homogeneous in that line: removing it only while
checking an equality does not change or reset its prescribed phase.

Let E_a,E_b shift the indicated input index by one, and let
(S h)(a,b,k)=h(a,b,k+1). These are ordinary translations of
unwrapped integer indices; k is never reduced modulo N.

## 2. The four literal F and E crossing currents

The actual coproducts are

    Delta F=F tensor 1+K^(-1) tensor F,
    Delta Ecal=Ecal tensor K+1 tensor Ecal.

Checked R intertwines the input coproduct with the same coproduct
in the switched color order. Taking one matrix entry gives

    f(a) r_s(a+1,b,k)
      +K_1(a)^(-1)f(b) r_s(a,b+1,k-s)
      =f(b+s k-1) r_s(a,b,k-s)
        +K_2(b+s k)^(-1)f(a-s k) r_s(a,b,k),      (2.1)

and

    K_2(b)e_1(a) r_s(a-1,b,k)
      +e_2(b) r_s(a,b-1,k+s)
      =K_1(a-s k-1)e_2(b+s k+1)r_s(a,b,k+s)
        +e_1(a-s k)r_s(a,b,k).                  (2.2)

These are exact zero-extended array identities with the actual
truncated edge functions. They include every corner and endpoint.
For example, (2.1) has target (b+s k,a-s k+1): raising the first
input gives its first term, raising the second input changes the
required transfer to k-s, and the two output insertions give its
right side. The same check with target (b+s k,a-s k-1) proves
(2.2). This derives the formulas directly from actual matrices,
not from a guessed q-hypergeometric summation identity.

They may also be checked on the strict interior as rational
identities of Q,x_1,x_2,Q^a,Q^b,Q^k, using the displayed proper
crossing ratios. At endpoints the truncated edges, rather than
unrestricted rational interpolation, specify the actual source.

For an explicit independent-variable verification put A=Q^a,
B=Q^b,C=Q^k. The three ratios r(a+1,b,k)/r, r(a,b+1,k)/r,
r(a,b,k+1)/r are, for s=+1,

    BC/x_2 * (1-x_1^2/A)/(1-x_1^2 C/A),
    A/(x_1 C) * (1-QBC)/(1-QB),
    -x_2 A/(Q x_1^2 BC)
                  * (1-QBC)(1-Qx_1^2 C/A)/(1-QC),

and for s=-1,

    x_2/B * (1-QAC)/(1-QA),
    x_1/A * (1-x_2^2/B)/(1-x_2^2 C/B),
    (1-QAC)(1-Qx_2^2 C/B)/(x_2(1-QC)).

They follow by canceling adjacent Gaussian and Pochhammer factors.
Use inverse ratios at the shifted arguments for negative shifts.
Dividing (2.1)--(2.2) by r then gives zero rational functions
after substitution of these ratios. In (2.2) the common q^(-1)
from e_i=q^(-1)(x_i^(-1)-Qx_i/Q^n) cancels. This establishes
the interior identity before any root or fixed-N evaluation.

## 3. Explicit transfer divergences

Define the following literal currents, including their coefficients:

    J_F,s=[K_1(a)^(-1)f(b)E_b-f(b+s k)] r_s,

    D_F,s=f(a)E_a+K_1(a)^(-1)f(b)E_b
             -K_2(b+s k)^(-1)f(a-s k)-f(b+s k).

Then (2.1) is exactly

    D_F,s r_s+(S^(-s)-1)J_F,s=0.                 (3.1)

For the raising current define

    J_E,s=[e_2(b)E_b^(-1)
                     -K_1(a-s k)e_2(b+s k)] r_s,

    D_E,s=K_2(b)e_1(a)E_a^(-1)+e_2(b)E_b^(-1)
                     -K_1(a-s k)e_2(b+s k)-e_1(a-s k).

Then (2.2) is exactly

    D_E,s r_s+(S^s-1)J_E,s=0.                    (3.2)

For instance S^s applied to the second term of J_E replaces its
coefficient by K_1(a-s k-1)e_2(b+s k+1), explaining both shifted
coefficients in (2.2). Operator order is as displayed.

The D operators still contain internal multiplication characters.
Thus summing these identities does not give a closed scalar Ward
operator on the uninserted partial sum alone. The natural exact
target includes the corresponding inserted moments.

## 4. The missing cyclic edge is an explicit wall source

Let W=E_(N-1,0) and put Ecyc_i=Ecal_i+kappa_i W. Define the
input and output two-leg cyclic coproduct matrices by the same
displayed coproduct expression in their respective color orders.
The actual checked matrix R_s obeys the exact equality

    R_s Delta_in(Ecyc)-Delta_out(Ecyc)R_s
      =R_s(kappa_1 W tensor K_2+kappa_2 I tensor W)
         -(kappa_2 W tensor K_1+kappa_1 I tensor W)R_s. (4.1)

It follows by subtracting the actual Ecal intertwining equation.
This is a retained boundary source, not an assertion that the
original R is an intertwiner for the completed colors.

If R(a,b;c,d) denotes its ordinary four-index entry, the right
side is precisely

    kappa_1 1_(a=0) K_2(b) R(N-1,b;c,d)
      +kappa_2 1_(b=0) R(a,N-1;c,d)
      -kappa_2 1_(c=N-1) K_1(d) R(a,b;0,d)
      -kappa_1 1_(d=N-1) R(a,b;c,0).             (4.2)

Thus the wrap is a change in the actual integer conservation
sector by N, with four fully specified endpoint currents. It is
not a periodic reinterpretation of the transfer bounds.

For equal colors this is kappa times [R_s,W tensor K+I tensor W].
At M=1 the actual and cyclic raising matrices agree, but dividing
this source by the meridian gap retains a generally nonzero
matrix. For the positive crossing and N>=3 one explicit entry is
from input (0,N-1) to output (N-1,N-1). After factoring only the
recorded common Cartan unit, its divided source is

    x^(-(N-1)) [x^(2-N)Q^2-1].                  (4.3)

At the prescribed complete x=q^(N-1), the expression in brackets
is Q-1 for odd N and -Q-1 for even N. It is nonzero for N>=3.
This proves a local first-normal source survives the missing-edge
division. It does not prove its class is nonzero after the global
framing Ward quotient or the actual cut.

## 5. Composition and the linear partial-current pushforward

For equal-color b-strand braids the iterated missing-edge operator is

    W_tot=sum_i I^(tensor(i-1)) tensor W_i
                                    tensor K_(i+1)...K_b.

For a word R_beta=R_m...R_1 the source composes by the exact rule

    [R_beta,W_tot]
      =sum_t R_m...R_(t+1)[R_t,W_tot]R_(t-1)...R_1. (5.1)

Spectator terms in W_tot commute through a local crossing because
it preserves the product K_iK_(i+1); the remaining terms are
exactly the local currents above. Mixed colors use (4.1) with
the color list switched after every crossing. Actual cups, caps
and pivots contract these matrix currents with their original
Hopf-adjoint rules from
[the exact Ward/cut construction](actual_borel_ward_cut_contraction.md).

There is an explicit linear current pushforward which is available
before any open-matrix-index identification. For a finite zero-
extended transverse array, or for its nondegenerate formal Gaussian
realization G, translation covariance gives

    G[(S^v-1)J]=0,
    G[h(S^v-1)J]=G[(S^(-v)h-h)J].               (5.2)

The first identity is finite reindexing, respectively formal Gaussian
integration by parts; the second follows by translating the entire
product hJ. It is valid with all rational insertions h regular on
the chosen formal chart. Therefore (3.1)--(3.2) give exact Ward
identities in the partially contracted inserted-moment module,
with separate finite and formal realizations. For the formal one,
first take the independent-variable interior identity just proved.
Endpoint indicators are not assigned an unjustified formal meaning;
they remain the explicit finite boundary sources to be compared.
For more than one internal coordinate use the displayed vector
translation v and sum the currents.

The global integral flow elimination has determinant +/-1; edge
current translations are consequently integral translations of the
remaining independent flow coordinates, with explicit affine offsets
obtained by the same closure solver. Keeping the two framing
coordinates external leaves their current operators present.
The Gaussian contraction kills only transverse divergences. It
does not integrate either framing direction or replace the retained
moment module by an unproved scalar Ward character.

This is a linear map of current identities. It is not a unital
map of finite matrix algebras into a scalar quantization. In
particular the fixed-N matrix relation (Ad_K)^N=I must not be
silently replaced by a nontrivial formal near-identity scalar action.
The interior all-level proper-ratio formalization unfolds those
fixed-N relations before taking H=Log Q as a formal parameter.

## 6. The exact remaining source-survival question

The local Ward currents, their cyclic endpoint source, composition,
and transverse linear pushforward are now specified. The full finite
operator-valued Hopf-adjoint diagram also exists. What is not yet
constructed is the comparison from this partially contracted
inserted-current module, with its remaining external currents,
to the cut Ward complex and its normal co-source.

There is an exact cancellation which makes this distinction necessary.
The proof that pivotal partial trace intertwines Hopf adjoints also
applies to Ecyc: it has the same K-weight, and gK^(-1)=K^(-N)
is central. Write C_beta=ptr(R_beta) for the actual fully closed
(1,1)-tangle matrix, with its fixed scalar zero-framing line retained.
It is scalar by the actual K,F Ward contraction. Hence

    ptr([Ecyc_tot,R_beta] K_tot^(-1))
          =[Ecyc,C_beta] K^(-1)=0.

Using the actual Ecal intertwining identity and (5.1), this gives
the whole meridian identity

    ptr([W_tot,R_beta] K_tot^(-1))=0.             (6.1)

It first follows away from kappa=0 by canceling that nonzero
scalar, then extends to M=1 through the regular whole matrix germ.
Thus the ordinary full contraction of the divided cyclic-wall
source is zero even when individual local matrices in (4.3) are
nonzero. A surviving source class must be relative to the marked
defect and its endpoints before this ordinary contraction; it
cannot be inferred from local nonzero matrix entries.

That map must carry the boundary source (4.2), canonical carry and
the actual normal cut row. Nondegeneracy of the transverse Hessian
alone does not supply it: the D operators in Section 3 visibly
retain inserted internal moments. A nonzero matrix such as (4.3)
can become exact or cancel after further contraction. Neither its
nonzero local coefficient nor Schur normalization proves a nonzero
selected global Bockstein class or a volume limit.

[Exact local-current audit](../experiments/audit_local_r_ward_transfer_currents.py).
[Results](../experiments/local_r_ward_transfer_currents_results.json).
