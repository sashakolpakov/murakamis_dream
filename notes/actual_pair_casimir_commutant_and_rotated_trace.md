# The full physical pair commutant, true box rotation, and its marked trace

29 October 2026. Every endomorphism commuting with the ORIGINAL two-head
E,F,K action is a polynomial in its Casimir, at EVERY level N>=2.
No generic semisimplicity or omission of projective normals is needed.
The literal bent pretzel boxes remain in this full algebra. Their
original source is one explicitly weighted Hermite-Casimir period.
This is a finite exact reduction, not a volume or asymptotic theorem.

## 1. The actual module and a generating middle weight

Put d=N-1, q=exp(pi i/N), Q=q^2, x=q^d, rho=q-q^(-1).
On the original balanced physical V_N use E=Ecal:

    E|a>=(Q^(-a)-1)|a-1>,
    F|a>=(1-Q^(a+1))|a+1>,
    K|a>=x Q^(-a)|a>,       0<=a<=d,

with outside-basis arrows omitted. The actual pair coproduct is

\[
 E_t=E_1K_2+E_2,\qquad F_t=F_1+K_1^{-1}F_2,
 \qquad K_t=K_1K_2,
 \qquad\Omega=F_tE_t+qK_t+q^{-1}K_t^{-1}.              \tag{1}
\]

Let W_T have the physical basis |a,T-a>, max(0,T-d)<=a<=min(d,T).
The K_t eigenvalue there is x^2Q^(-T)=Q^(d-T). Its eigenvalue ONE
occurs ONLY on W_d: the other possible degrees d+N and d-N lie
outside [0,2d]. Thus an arbitrary E_t,F_t,K_t intertwiner preserves
W_d, even if integer-degree preservation was not assumed.

The following surjections are literal bidiagonal matrix facts:

\[
 E_t:W_{T+1}\twoheadrightarrow W_T\quad(0\leq T<d),
 \qquad
 F_t:W_T\twoheadrightarrow W_{T+1}\quad(d\leq T<2d).    \tag{2}
\]

For the first use domain columns a=0,...,T and target rows a=0,...,T.
The second-head E entry has nonzero diagonal
Q^(-(T+1-a))-1; the other E entry is strictly off that diagonal.
For the second use source a=T-d,...,d-1 and target a+1. The
first-head F entry has diagonal 1-Q^(a+1), all nonzero, and the
second-head term is off diagonal. These prove the two maximal ranks,
including every composite and even N. Consequently

\[
 V_N\otimes V_N
   =\sum_{r=0}^d E_t^r W_d+\sum_{r=1}^d F_t^r W_d.     \tag{3}
\]

This is generation by a specified physical weight space, not a claim
that some abstract projective generator exists.

## 2. Exact commutant theorem, with all Jordan derivatives retained

The middle block J=Omega|_(W_d) is the original complex symmetric
tridiagonal matrix, with offdiagonal

    J[a,a+1]=J[a+1,a]=-(1-Q^(a+1))^2,  0<=a<d.

All these entries are nonzero. In the vectors e_0,J e_0,...,J^d e_0,
the k-th vector has last possible nonzero component k, equal to the
nonzero product of the first k offdiagonals. They are a basis.
Hence any X_d commuting with J is a UNIQUE polynomial f(J), deg f<N:
choose f by X_de_0=f(J)e_0 and commute with J on this cyclic basis.

Now let X commute with E_t,F_t,K_t. It preserves W_d by section 1
and commutes with Omega. Choose that f and put Y=X-f(Omega).
Then Y annihilates W_d and commutes with E_t,F_t. Equation (3)
forces Y=0 on the ENTIRE pair. We have therefore proved

\[
 \boxed{\operatorname{End}_{E_t,F_t,K_t}(V_N\otimes V_N)
       =\mathbb C[\Omega],\qquad \dim\mathbb C[\Omega]=N.} \tag{4}
\]

It follows in particular that every such endomorphism preserves full
integer degree and is complex symmetric in the original pair basis.
The actual Casimir is symmetric on every physical block.

The familiar complete characteristic polynomial can also be recovered
without a representation-theoretic endomorphism assertion:

\[
 P_N(z)=2T_N(z/2)+2
       =\prod_{j=0}^{d}(z-c_j),\qquad
 c_j=q^{2j+1}+q^{-2j-1}.                               \tag{5}
\]

For example continue the explicit highest-weight N-module in q; its
generic pair highest weights 2d-2j give these limiting middle-block
eigenvalues. The middle characteristic polynomial is (5). The cyclic
basis makes it also the minimal polynomial, and (3) propagates its
vanishing to the full pair. Alternatively its original continuant
recurrence gives the same polynomial. Thus the only simple root is
-2 for odd N; every other distinct root is DOUBLE. Equality (4) is
the full Hermite algebra C[z]/P_N, not the algebra of values on its
distinct roots. In particular projective first derivatives survive.

## 3. Literal turn rotation agrees with the charge-block formula

Keep the actual pair turns, with their ORIGINAL scalars:

    p_ab=N x^(-b) delta_(a+b,d),
    ell_ab=x^a/N delta_(a+b,d).

They are the original invariant cup and cap; E_t p=F_t p=0,
K_t p=p and the corresponding cap identities follow directly from
their displayed entries. They obey the two snake identities.

For an actual Hopf box B, define its genuine bend by

\[
 \mathcal R(B)=(I^{\otimes2}\otimes\ell)
              (I\otimes B\otimes I)
              (p\otimes I^{\otimes2}).                 \tag{6}
\]

Composition of the just specified intertwining matrices makes this
an E_t,F_t,K_t intertwiner. The cup adds integer degree d and the
cap removes d. No separate quantum-group covariance hypothesis on
an arbitrarily framed head is used. Direct contraction gives

\[
 \mathcal R(B)_{(a,b);(c,e)}
       =x^{a-e} B_{(b,d-e);(d-a,c)}.                    \tag{7}
\]

By (4) the original B is symmetric. Its degree support and
a+b=c+e turn (7) into the concrete source-normalized rotated box

\[
 \boxed{(Z_B)_{(a,b);(c,e)}
       =x^{c-b-d}B_{(d-a,c);(b,d-e)},\qquad
       Z_B=x^{-d}\mathcal R(B)\in\mathbb C[\Omega].}     \tag{8}
\]

The scalar x^(-d) is retained; it is part of the source port convention.
Both original N factors cancel in (6). Formula (8) is injective as a
reshuffling of all four indices, so it is a linear automorphism of
the N-dimensional algebra (4). It is NOT an algebra homomorphism.
For example

\[
 Z_I=x^{-d}p\ell,\qquad Z_{R^{-1}}=x^{-d}R.             \tag{9}
\]

For the second identity use the literal original inverse
R^(-1)=P conjugate(R) P and factorial reflection
F_(d-a)=N(-1)^a Q^(a(a+1)/2)/F_a. After these substitutions the
factorial ratio is exactly the original positive crossing ratio.
Writing k=a-e=c-b, the residual Q exponent, before reducing modulo
N, is b(e+1)-(b+k)N. The remaining Cartan/x factors use
kappa^2=x^d and x^2=Q^(-1), giving precisely (9), without a parity
or normalization exception.

In the pretzel notation T=d+h, I_h=[max(0,h),min(d,d+h)], put
S_h=diag_(a in I_h)x^a and let P_h reverse a to T-a. For the
literal transfer M_B in the
[original all-width source](actual_odd_pretzel_augmented_transfer_source.md),
equation (8) says EXACTLY

\[
 Z_B|_{W_{d+h}}=P_hS_hM_B^hS_h^{-1}P_h.                \tag{10}
\]

This fixes the true turn conjugation rather than identifying a
reshuffled positive tensor with a physical crossing by analogy.

The same four-index formula also supplies its exact inverse:

\[
 Z_{Z_B}=x^{-2d}B.                                    \tag{10a}
\]

Indeed the two exponents in the composition add to -2d and all
four original indices return. Consequently Z_R=x^(-d)R^(-1) and
Z_(p ell)=x^(-d)I as well. These are coherent full-Hermite Fourier
identities; the rotation is still not multiplicative.

## 4. The ORIGINAL fixed-root trace is an explicit Hermite period

Let g=K^(1-N) be the ORIGINAL physical pivot and define

\[
 \phi(f)=\frac1N\operatorname{Tr}_{V_N\otimes V_N}
                 [(I\otimes g)f(\Omega)].              \tag{11}
\]

At this root K^N=(-1)^d I, hence g=(-1)^d K EXACTLY.
For each distinct double node c in (5), retain both f(c) and f'(c).
Then

\[
 \boxed{\phi(f)=(-1)^d\sum_{c\ {\rm double}}
       \{(4-c^2)f'(c)-c f(c)\}
       +\mathbf1_{N\ {\rm odd}}f(-2).}                 \tag{12}
\]

Here is an independent finite-matrix derivation, including its germ
scope. Use a generic variable z near q and the explicit ordinary
highest-weight N-module with K_a=z^d z^(-2a), F_a=1-z^(2a+2),
and E_a=z^(-N)-z^N z^(-2a), missing endpoints omitted. It specializes
to the original module. Its K-pivotal partial trace of f(Omega_z)
is a scalar C(z) I. This follows directly from the coproduct:
tracing [f(Omega_z),E_1K_2+E_2]=0 over head2 yields [C,E_1]=0;
the F equation, K conservation and cyclicity of the head2 trace yield
[C,F_1]=0. Distinct K weights and nonzero internal F entries make
the partial trace scalar. No generic Schur assertion at the root
is used.

Explicitly K conservation gives
A K_1^(-1)=K_1^(-1)K_2^(-1) A K_2 for A=f(Omega_z), so

    Tr_2 K_2[A,K_1^(-1)F_2]
       =K_1^(-1) Tr_2(A K_2F_2-K_2F_2 A)=0.

Tracing the F coproduct commutator now gives [C,F_1]=0 directly.

For generic z, solve the bidiagonal highest-weight equations and
take their F descendants. They give one summand of highest weight
2d-2j for each j=0,...,d; their dimensions sum to N^2 and their
distinct generic Casimirs prove independence. Their K traces are
[2d-2j+1]_z. Taking one further K trace therefore gives

\[
 C(z)=\frac{\sum_{j=0}^d[2N-1-2j]_z
             f(z^{2N-1-2j}+z^{-2N+1+2j})}{[N]_z}.      \tag{13}
\]

The actual finite matrices make C(z) regular at z=q. Keep f fixed
and differentiate this removable ratio in log z. The denominator
derivative is -2N/rho. At a pair with r=2j+1 and m=2N-r, the
dimension weights cancel at the root; their derivatives sum to
2Nc/rho. The sum of weight times the node derivative is
2N(c^2-4)/rho. Their ratio is (4-c^2)f'(c)-cf(c).
At the odd self-paired m=N, the removable ratio contributes f(-2).
Finally multiply by (-1)^d to replace K by the ACTUAL fixed-root g.
For odd N this sign is one. This proves (12).

This use of a generic K trace COMPUTES A FIXED-ROOT FUNCTIONAL. It
does NOT differentiate the original whole q-dependent source
g(z)=K(z)^(1-N), and does not identify that source germ with a
generic K-pivotal germ. Any such q-normal-jet assertion requires its
own pivot derivative. It is unnecessary for (11)--(12).

In particular phi(1)=0, phi(L_N)=N^2 and
phi(R)=kappa x^(-d), with the actual crossing and auxiliary-circle
normalizations. Also phi(p ell)=1. The trace weights in (12) have
only polynomial size:

\[
 |\phi(f)|\leq (N+1)\max_c|f(c)|+2N\max_{c\ {\rm double}}|f'(c)|.
                                                               \tag{14}
\]

There is no exponentially costly hidden source conversion in this
period. This does not control the actual rotated nodal values or
their phases for a given family of boxes.

There is a useful exact endpoint form of the SAME functional. If
r_f is the degree-at-most-d remainder of f modulo P_N, then

\[
 \boxed{\phi(f)=(-1)^dN^2[z^d]r_f(z)
                    =(f(J))_{0,d},\qquad J=\Omega|_{W_d}.} \tag{14a}
\]

To see the coefficient identity directly, at a double c the factor
Q_c=P_N/(z-c)^2 has
Q_c(c)=N^2/(4-c^2), Q_c'(c)/Q_c(c)=c/(4-c^2), as follows by
differentiating the elementary Chebyshev equation. Thus the residues
of f/P_N, multiplied by (-1)^d N^2, are exactly (12). At odd N,
P_N'(-2)=N^2 supplies the simple-node term. Their sum for the proper
fraction r_f/P_N is its coefficient of z^(-1) at infinity,
namely [z^d]r_f. Finally the tridiagonal path from 0 to d has length
at least d, and its sole length-d coefficient is

    product_(a=1)^d[-(1-Q^a)^2]=(-1)^d N^2.

This proves the last identity in (14a). It is the original selected
endpoint matrix element; it is not a positive trace or permission
to select only one logarithmic/Fourier winding of a residue formula.

## 5. All-width pretzel reduction, including the original mark

The original source theorem gives the transfer trace with D_h=diag x^(2a).
Under (10),

    P_h D_h P_h=x^d (I tensor g)|_(W_(d+h)).

Conjugating the PRODUCT of all transfers by the SAME S_h,P_h and
retaining its original prefactor x^((s-1)d)/N proves

\[
 \boxed{\mathcal A_{s,N}(B_1,\ldots,B_s)
       =x^{sd}\phi(Z_{B_1}\cdots Z_{B_s}).}             \tag{15}
\]

This uses every h=-d,...,d and the unrestricted original marked row
until the already proved whole-degree restriction. Its original
external chi_N is multiplied afterwards without modification.

There are two convenient normalization conventions for this same
rotation. For the unscaled genuine quarter-turn mathscrR(B)=x^d Z_B,
equation (15) is equivalently phi(product_i mathscrR(B_i)), with NO
external x phase. The explicit polynomial z_N in the
[complete-base calculation](actual_pretzel_complete_base_casimir_polynomial.md)
uses this unscaled mathscrR convention. Thus its source-normalized
Z_B polynomial here is x^(-d)z_N. These scalar conventions must not
be mixed.

Writing Z_(B_i)=z_i(Omega), (12) makes (15) an explicit finite sum:
at each double c, its derivative is
sum_i z_i'(c) product_(k!=i) z_k(c), alongside the value product;
the odd simple node contributes its full product. Thus all s boxes
couple through the same actual Casimir channel, with the original
normal source retained. No independent summation of unphysical
channel maxima, deletion of a zero value's derivative, or assumed
positive pairing is involved.

The [audit](../experiments/audit_actual_pair_casimir_commutant_and_rotated_trace.py)
uses original finite generators to check the full E/F/K commutant,
the middle cyclic basis and both generating surjections, literal
rotations of a complete polynomial basis, source-normalized crossing
rotation, fixed-root trace on values AND derivatives, and the marked
all-width product identity. The general geometric growth estimate
for the rotated channel packets remains a separate task.
