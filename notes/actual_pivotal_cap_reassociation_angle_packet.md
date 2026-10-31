# An ordinary pivotal cap coherently collapses reassociation to one angle weight

29 October 2026. Contracting the original ordinary pivotal cap with
the actual three-head reassociation packet annihilates every middle
input except the top index d=N-1. The surviving map is a phase times
weighted truncated addition. In the source-fixing quarter-factorial
metric its squared coefficient is exactly ONE positive affine-angle
weight. All intermediate terms have been summed coherently first.

The inverse-packet/cup move has an equally explicit bottom-index
selection and the same one-weight energy. These are exact local
operator/source identities for arbitrary exteriors, not merely scalar
normalizations. The marked cap is different: its complete retained
packet is given below and is not replaced by the ordinary cap.

## 1. Actual packet, source and metric conventions

Put q=exp(pi*i/N), Q=q^2, d=N-1, x=-q^-1=q^d, N>=2,
F_a=(Q;Q)_a and s_a=|F_a|. Keep the original finite transfers

    C'_12|a,b>=sum_r x^-r [b+r choose r]_Q |a-r,b+r>,
    (C'_12)^-1|a,b>
       =sum_r (-1)^r Q^[r(r-1)/2]x^-r
                         [b+r choose r]_Q |a-r,b+r>,        (1)
    0<=r<=min(a,d-b).

These are the original nilpotent Euler matrices and their full
inverse, including strict head endpoints. The actual packet is

    A=(C'_23)^-1 C'_12.                                    (2)

Its full entry, derived by its UNIQUE intermediate state, is

    |a,b,c> -> |a-r,b+r-s,c+s>,
    A=(-1)^s Q^[s(s-1)/2]x^[-(r+s)]
                     [b+r choose r]_Q[c+s choose s]_Q,      (3)
    r<=min(a,d-b), s<=min(b+r,d-c), r,s>=0.

The normalized original ordinary cap and cup are

    ellhat= sqrt(N) ell,
    ellhat|u,v>=(xQ)^-u/sqrt(N) delta_(u+v,d),
    phat=p/N^(3/2),
    phat=sum_(u=0)^d x^(u-d)/sqrt(N) |u,d-u>.              (4)

Indeed the literal original turns are
ell|u,v>=x^v g_u/N delta_(u+v,d), p_(u,v)=N x^-v delta,
g_u=x^-d Q^-u. Thus(4) retains the original pivot, not a cap
with a favorable substituted phase. The normalized cap and cup
both have norm1. Literal ell and p are restored by their stated
N powers; all external Cartan/framing/peripheral lines are unchanged.

Use the PHYSICAL gauge and squared metric

    B_a=L_a^-1/4, h_a=B_a^2=sqrt(N)/s_a,
    L_a=s_a^2/N.                                          (5)

Root reflection gives B_a B_(d-a)=1. These original turns are
fixed by B on paired legs. Hats on maps below mean conjugation
by B on their physical input/output legs. This is not the length
normalization b_l=B_l/D_l and is not the different tame-current
metric L^(1/2).

## 2. Exact cap selection, including the coherent root sum

Define K=(ellhat_12 tensor I_3) A. For every physical input,

    K|a,b,c>=0 unless b=d and a+c<=d.                     (6)

In the surviving case n=a+c,

    K|a,d,c>=N^-1/2 (-1)^a Q^[a(a-1)/2-a]x^(-2a)
                                      [n choose a]_Q |n>. (7)

Proof. The cap condition in(3) fixes s=a+b-d. If this is negative,
or s>d-c, the contraction is zero. Otherwise its allowed r range
is exactly0,...,d-b. The ordinary pivotal cap phase supplies Q^r,
and all the remaining factors are independent of r. Its complete
coherent sum is

    sum_(r=0)^(d-b) Q^r[b+r choose r]_Q
                                  =[N choose b+1]_Q.       (8)

For completeness, q-Pascal gives
[j+1 choose b+1]-[j choose b+1]=Q^(j-b)[j choose b].
Sum from j=b to d. At the primitive root the resulting Gaussian
polynomial is zero for b<d and one for b=d. Its intermediate
factorials have no zero denominator; [N choose N]=1 is its
literal polynomial value. This works at every even and composite
level as well.

Thus b=d, r=0, s=a, n=c+a, with the strict condition n<=d.
Substitution of the original cap coefficient gives precisely(7).
This is cancellation of the full finite packet, not one selected
term or an assumed homogeneous-source quotient.

## 3. The doubled packet has exactly one positive angle weight

Define w_d(i,j,k)=1/(s_i s_j s_k), i+j+k=d. Applying(5) to(7)
gives the exact entry

    Khat_(n;(a,b,c))
       =delta_(b,d)delta_(n,a+c<=d)
           q^[a(n-N-1)] sqrt(w_d(a,c,d-n)).                 (9)

Indeed the squared gauge ratio is h_n/(h_a h_d h_c)=s_a s_c/s_n.
Consequently

    |Khat_(n;(a,d,c))|^2
      =(1/N)|[a+c choose a]_Q|=w_d(a,c,d-a-c).              (10)

For the LITERAL original cap ell the right side is w_d/N, because
ell=ellhat/sqrt(N). No original scalar line was discarded.

The complete doubled input Gram retains the mixed copies:

    (Khat^*Khat)_(a,d,c ; a',d,c')
      =delta_(a+c,a'+c')
         q^[a'(a'+c'-N-1)-a(a+c-N-1)]
         sqrt(w_d(a,c,d-a-c)w_d(a',c',d-a'-c')).            (11)

All other middle-input rows/columns are zero. The positive trace
on the one remaining output has supplied the UNWRAPPED constraint
n=n'. It admits either exact N or2N Fourier character expression,
since n,n' lie in0,...,d. This does not identify n=n' with a
global triangulation edge sum2d. The non-diagonal terms of(11)
have not been dephased.

Rows of Khat have disjoint total-input-degree support, so

    Khat Khat^*=diag(R_n),
    R_n=sum_(a=0)^n w_d(a,n-a,d-n),
    ||Khat||_op^2=max_n R_n,
    ||Khat||_HS^2=sum_n R_n=Z_(3,N).                        (12)

Here Z_(3,N) is the positive affine angle-simplex partition, with
total d and zero angles retained. Thus the EXACT map has the
one-tetrahedron energy exponent

    log||Khat||_op^2=log||Khat||_HS^2+O(logN)
                                =N v_3/pi+O(logN).          (13)

The uniform factorial estimate and the unique simplex maximum
at thirds prove(13); no isolated numerical saddle is a premise.
Equation(12), not a separate entrywise Cauchy estimate, gives its
quantitative all-exterior boundary norm.

## 4. The inverse-packet cup move

Let J=A^-1(phat_12 tensor I_3). Its exact output selection is

    J|n> supported on |a,0,c>,
    a+c=n+d, n<=a<=d,
    J_(a,0,c ; n)=N^-1/2 x^[2(a-d)] [c choose d-a]_Q.      (14)

Proof. Write the cup index as p and apply C'_23 followed by
(C'_12)^-1. The desired output fixes s=d-a-b and p=a+r.
The remaining finite r sum is

    sum_(r=0)^b (-1)^r Q^[r(r-1)/2][b choose r]_Q
                                                    =(1;Q)_b.

It is zero unless b=0; for b=0 one has r=0,p=a,s=d-a and
c=n+s. Substitution gives(14), with every inverse phase retained.
Thus this is an exact cup/current cancellation, not an adjoint
claimed from a nonunitary packet.

In the SAME physical metric(5),

    |Jhat_(a,0,n+d-a ; n)|^2
                              =w_d(n,d-a,a-n).             (15)

To check it directly, the squared gauge ratio is
h_a h_0 h_c/h_n=N s_n/(s_a s_c). Multiplying the squared
coefficient in(14) and using s_a s_(d-a)=N gives(15).
It follows that Jhat^*Jhat=diag(R_(d-n)), so its operator/HS
norms have the same exact one-weight partition as(12). The
literal original cup p restores the factor N^(3/2) in amplitude,
or N^3 in energy. These polynomial factors remain explicit.

## 5. What is retained at the marked cap

The actual full marked row is m_(u,v)=x^v/N^2, WITHOUT a degree
delta. It cannot use(8). Its complete packet on arbitrary input
has output n=c+s, 0<=s<=d-c, and the exact coefficient

    (m_12 A)_(n;(a,b,c))
      =N^-2 (-1)^s Q^[s(s-1)/2]x^[b-2s]
         [c+s choose s]_Q
           *sum_(r=max(0,s-b))^(min(a,d-b)) [b+r choose r]_Q. (16)

An empty interval means zero. This follows directly from(3) and
the unrestricted original row; no source component is omitted.
It is the remaining finite current packet when a marked boundary
is present. Only if the FULL exterior has already forced pair
degree d can the corresponding restricted marked row be used.
Even then its r sum lacks Q^r and equals (Q^(-(d-b));Q)_(d-b),
not the delta in(8). It is generally nonzero away from b=d.

Thus the ordinary cap elimination is source-exact and useful,
but does not delete the last marked source or its normal currents.
If a beta or divided-Ward factorization is used to express(2),
all its terms must add back to(6)--(16). Keeping only a bare
balanced residue would not establish these identities.

## 6. Positive multiplication form and iteration scope

Write sigma_a=q^[a(a-N-1)] and g_j=q^[j(j-1)/2]. Since
q^(ac)=g_(a+c)/(g_a g_c), the unitary port phases in(9)
can be displayed explicitly. After transporting those phases,
the positive two-input part is

    T^+_(n;a,c)=N^-1/2 delta_(n=a+c<=d)
                              sqrt(s_n/(s_a s_c)).         (17)

For W_j=1/sqrt(s_j) it is exactly

    T^+=N^-1/2 W^-1 M(W tensor W),

where M is multiplication in C[z]/(z^N), in its canonical
monomial basis. Consequently these positive kernels associate
exactly, and their internal factorials telescope on a rooted
tree. Actual port phases and the removed middle |d> registers
must still be retained in the original diagram. They are not
declared globally canceled by(17).

The [complete cap-tree calculation](actual_cap_tree_angle_energy.md)
gives the arbitrary-width boundary-tree energy with these original node types. This does
not assert that every signed braid reduces to such a tree:
overlapping recoupling cycles, Gaussian feedback and especially
the full marked packet(16) remain. No broad knot survival or
sharp whole-source volume estimate follows merely from this
local contraction.

[Audit](../experiments/audit_actual_pivotal_cap_reassociation_angle_packet.py):
full original finite packet matrices, ordinary cap and cup source,
complete phases and forced indices, exact mixed-copy Gram,
one-weight norms, and the unrestricted marked packet.

The finite audit checks seven levels N=2,...,8 and all 1,295 three-head
input columns, checking the full original cap and inverse-cup matrices,
the retained marked packet, phases, mixed-copy Gram and one-weight
norms. The algebraic proofs above establish the all-level statements;
these finite checks are supplementary.