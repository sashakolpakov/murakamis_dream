# Exact longitude insertion and the regulator action of the actual state

Research note, 26 October 2026. This continues the
[marked braid correspondence](marked_braid_holonomy.md) and
[complete fundamental-cycle comparison](crossing_fundamental_cycle.md).
It proves an exact meridian-shift insertion formula in the actual
finite state, identifies its classical coordinate with the preferred
longitude, and fixes the norm of a compatible geometric logarithmic
action. The selected finite period's geometric contribution is
still unproved; this is not a proof of the volume conjecture.

The construction uses the literature ADO state already fixed in
[the normalization audit](kashaev_ado_pointing.md). It introduces
neither an ordering of an arbitrary classical polynomial nor a
replacement state.

## 1. The meridian shift is an exact finite insertion

Fix a b-strand braid closing to a knot, with writhe w. Put

    q=exp(pi*i/N), Q=q^2, x=q^alpha, M=-qx,
    kappa_D=w-b+1.

The permutation of a knot braid is a b-cycle, hence kappa_D
is even. The actual reduced zero-framed state F_N(M) is the
cut scalar. In the balanced factorial basis it can equally
be written with a constant cut vector and normalized average.
Every nonzero term then has matching cut input and output
indices: total integer weight is conserved at every crossing.
Denote the resulting closed state set by S_N and its full
weight, including trace, framing, and 1/N, by W_N(x;s).

For a crossing with input a,b and shift k use
A=Q^a,B=Q^b,C=Q^k,X=x^2. Define the rational functions

    tau_+=BC/x * (1-QX/A)/(1-QXC/A),
    tau_-=x/A * (1-QX/B)/(1-QXC/B).                 (1.1)

Then, exactly at every level N>=2,

    F_N(qM)=sum_(s in S_N) L_D(q,x;s) W_N(x;s),
    L_D=q^(-kappa_D) x^(-w)
                              product_crossings tau_sign^(-1). (1.2)

The insertion is a fixed rational expression in q,x and the
internal monomials. Its formula does not grow with N. Its
meaning at a zero or pole is the cancelled whole term, as
specified in Section 2, not evaluation of separate quotients.

### Direct proof, including the square-root and framing factors

The exact coefficients in the preceding notes give

    r_+(qx)/r_+(x)
      =q^(-a-b-k)(1-QXC/A)/(1-QX/A),
    r_-(qx)/r_-(x)
      =q^(a+b-k)(1-QXC/B)/(1-QX/B).                 (1.3)

If c is the first output index, respectively b+k or b-k,
both equations become

    r_sign(qx)=x^(-sign)q^(c-a) r_sign(x)/tau_sign. (1.4)

The factor q^(c-a), sometimes written as a square root of
a shape monomial, telescopes without a sign ambiguity. Let

    J(a_1,...,a_b)=-sum_j j*a_j.

For either crossing, c+d=a+b as an equality of integers,
and J_out-J_in=c-a. Every closed state therefore has

    product_crossings q^(c-a)=1.                   (1.5)

This uses the actual unwrapped indices and their finite support;
it does not infer a sign by taking a square root after cyclic
specialization.

The pivotal trace contributes q^((1-N)(b-1)) under x->qx,
and the residual zero-framing factor contributes q^(w(N-1)).
Their product is

    gamma_N=q^((N-1)kappa_D)=q^(-kappa_D),           (1.6)

because q^N=-1 and kappa_D is even. Combining (1.4)--(1.6)
proves (1.2). No summation index was shifted, so no endpoint
term is omitted. Away from the roots the auxiliary finite cut
lift has the same identity with gamma_N in place of q^(-kappa_D),
or with z^kappa_D q^(-kappa_D) when z=q^N. That central factor
must be retained before q^N=-1.

There is a useful cancellation in (1.2). Put Y=M^2=QX. Then

    L_D=q^(-kappa_D)
       product_positive (1-YC/A)/(BC(1-Y/A))
       product_negative A(1-YC/B)/(1-Y/B).          (1.7)

Thus the insertion uses the squared meridian, with no residual
x or square root. Its N-fold cyclic norm is exactly one on
every closed state. The
[squared-meridian descent](even_meridian_norm_descent.md) proves
F_N(-M)=F_N(M), descends the actual minimal operator to Y, and
retains the full ADO state's even-level sign. Its natural root
norm extension has degree N rather than 2N.

## 2. Cancellation at the ideal color and higher shifts

Write r_sign=J_sign(z_sign;Q)_k, where J_sign denotes the
explicit monomial times Gaussian binomial in the actual formula,
defined without dividing by the Pochhammer. Put
z_+=QX/A, z_-=QX/B. Adjacent product cancellation proves

    r_+/tau_+=(x/(BC)) J_+ (Qz_+;Q)_k,
    r_-/tau_-=(A/x) J_- (Qz_-;Q)_k.                 (2.1)

These are finite Laurent expressions in x, even when the
individual ratios in (1.1) are singular. For k=0 both
Pochhammers are one; for k>0 cancel the first factor and add
the last. This proves the extension of (1.2) to M=1 while
retaining its whole meridian germ.

For j>=0 there is the exact ordered-insertion identity

    F_N(q^j M)=sum_s W_N(x;s)
                        product_(r=0)^(j-1)L_D(q,q^r x;s).      (2.2)

The local cancelled forms are

    r_+ product_r tau_+(q^r x)^(-1)
      =J_+ (Q^j z_+;Q)_k (x/(BC))^j q^(j(j-1)/2),
    r_- product_r tau_-(q^r x)^(-1)
      =J_- (Q^j z_-;Q)_k (A/x)^j q^(-j(j-1)/2).     (2.3)

They follow by telescoping a finite rectangular product. The
external multiplier for the right side of (2.3), when summed
with the old trace and framing weights, is

    gamma_N^j x^(-jw)q^(-w j(j-1)/2).

All these formulas preserve even and composite levels and all
finite support endpoints.

For a specified Ore operator P=sum_j a_j(q,M)T^j, TM=qMT,
its action on F_N is consequently the same actual period with
the inserted expression

    sum_j a_j(q,M) product_(r=0)^(j-1)L_D(q,q^r x;s).             (2.4)

Thus T is an actual quantum peripheral insertion in the
literature state. Equation (2.4) neither assumes that its
classical polynomial annihilates each individual state nor
identifies the minimal operator's classical components.

### The full ADO normalization remains explicit

For N_N(M)=d_N(M)F_N(M), use the already proved gauge

    g(q,M)=d_N(qM)/d_N(M)
          =-q^(-1)(q^2M^2-1)/(M^2-1).

Its insertion is g(q,M)L_D. This retains the entire factor
d_N=i^(N+3)M^(N-1)/(1+M^2+...+M^(2N-2)). The full state may
have poles elsewhere on the root orbit, so its identities are
meromorphic whole-germ identities. At a generic classical
meridian g->-1; the full and reduced classical shift variables
therefore differ by a sign. No numerical specialization erases
that marked distinction.

## 3. Its classical symbol is the preferred longitude

Let q->1 in the rational insertion, with the internal
coordinates held fixed. Then x=-M and

    ell_intr=x^(-w)/T_over,
    T_over=product t_sign,
    t_+=BC/x*(1-x^2/A)/(1-x^2C/A),
    t_-=x/A*(1-x^2/B)/(1-x^2C/B).                   (3.1)

The exact cancellation (1.5) fixes the sign of this symbol.
There is no remaining arbitrary square root.

Here is a vector proof of its marking. In the balanced physical
coordinates of the previous note,

    K=x/A, e=(x^(-1)-K)p, f=(1-A)/p.

The raw meridian matrix G=b_-^(-1)b_+ obeys

    G (p,1)^t=x^(-1)(p,1)^t.

Thus the canonical momentum p is the raw projective eigenflag.
After the prefix transport B_(-,j-1), use the global vectors

    v_j=B_(-,j-1)^(-1)(p_j,1)^t.

Their actual meridians mu_j=-H_j have eigenvalue M^(-1)
on these vectors. Direct substitution in both crossing maps
gives

    v'_under=-mu_over^(-sign) v_under,
    v'_over=t_sign v_over.                         (3.2)

For example at a positive crossing,
H_1^(-1)b_(-,1)^(-1)=b_(+,1)^(-1), whose second row is
(0,1). Hence its under-vector is already normalized with
scalar one before replacing H_1 by -mu_1. The over scalar
is p'_2/p_1, exactly t_+ in (3.1). The inverse crossing gives
t_- and the same minus sign. This proves (3.2) as a rational
identity, with the prefix transports included.

Follow the single knot through its braid and closure. Let W
be the left-ordered product of mu_over^(-sign) encountered
at the underpasses. Each crossing supplies one minus sign,
and each supplies one factor t_sign at its overpass. Since
the critical tuple closes, (3.2) gives

    1=(-1)^c T_over * eigenvalue(W),                (3.3)

where c is the crossing number. The positively oriented
blackboard parallel has holonomy W^(-1): its Wirtinger word
lists mu_over^(sign) in encounter order, the inverse of this
left-ordered vector transport. Its linking number is w.
Therefore the preferred longitude is

    lambda=W^(-1)mu^(-w).                          (3.4)

This also follows by pushing the parallel curve along the
diagram: an underpass contributes its over-meridian with the
crossing sign, and removing the writhe removes mu^w.

On the selected M^(-1)-flag, (3.3)--(3.4) give

    eigenvalue(lambda)=(-1)^c M^w T_over
                      =x^w T_over=ell_intr^(-1),    (3.5)

using c congruent to w modulo two. On the other peripheral
flag, with meridian eigenvalue M, the eigenvalue is ell_intr.
Consequently

    (M,ell_intr) is the marked preferred peripheral pair.       (3.6)

The source's cut flag and the flag in (3.6) are explicitly
different at generic M. At completeness they coalesce, and
the rational identity extends on the augmented chart. This
fixes the Weyl inversion that a wedge calculation alone
could not detect.

The geometric peripheral image of the actual classical
critical correspondence is therefore the marked geometric
A-curve in these variables. This is a statement about that
critical correspondence. It is not a claim that every minimal
annihilator of its selected quantum period retains this component.

## 4. A source-compatible logarithmic action

Put h=Log Q=2pi*i/N and u=Log M. Use independent integral
state variables k_i, with t_i=Q^(k_i), xi_i=Log t_i.
The actual incidence/weight-conservation lattice is integral;
its kernel has an integral basis. Choose these coordinates
before passing to logarithms, retaining any N-dependent purely
imaginary affine offsets.

The leading action derived from the actual coefficients has
the form

    S=G(xi,u)+sum_j eps_j Li_2(z_j),                (4.1)

where z_j are monomials with modulus-one constants, and G
is a quadratic form with real coefficients, a purely imaginary
linear term, and a real constant. The real constant includes
the retained Li_2(1) and framing constants.

For example, in a positive crossing with a=Log A,b=Log B,
c=Log C, the balanced expression uses

    G_+=ab+(a-b)c-c^2/2-u(a+b+c)-pi*i(a+b),
    Phi_+=Li_2(B)+Li_2(C)+Li_2(M^2/A)
                       -Li_2(BC)-Li_2(M^2C/A)-Li_2(1).

The negative expression uses

    G_-=-ab+u(a+b-c)+pi*i(a+b-c),
    Phi_-=Li_2(A)+Li_2(C)+Li_2(M^2/B)
                       -Li_2(AC)-Li_2(M^2C/B)-Li_2(1).

These signs follow from Log x=u+pi*i in the actual formulas.
The pivotal term is 2pi*i sum_(closed legs)Log A_j and
the remaining framing term is
2pi*i*kappa_D*u-2pi^2*kappa_D. Subleading terms remain
in the exact quantum weights; (4.1) only describes their
already specified leading logarithmic action.

On an exponentiated critical branch,

    partial_(xi_i)S=2pi*i*n_i, n_i in Z.

The integers are locally constant on its logarithmic cover.
Define

    S_flat=S-2pi*i sum_i n_i xi_i.                  (4.2)

This is compatible with the *same* actual discrete period:
at every actual state, on its unwrapped lift xi_i=h k_i,

    exp((S_flat-S)/h)=exp(-2pi*i sum_i n_i k_i)=1.   (4.3)

No coefficient or boundary factor is changed. Equation (4.3)
is a discrete character identity; it is not a claim that this
character is an ordinary rational gauge for generic q. It
identifies permissible logarithmic action sheets of the same
finite data. In particular it does not choose a global steepest
descent cycle or its coefficient.

After restriction to this log-critical branch,

    dS_flat=2v du, v=Log ell_intr.                  (4.4)

The factor two is forced by the actual meridian half-step
u->u+h/2 and by (1.3), not inferred from an analogy with a
classical polynomial.

## 5. An exact logarithmic identity fixes the geometric action norm

For the same compatible logarithms and dilogarithms,

    D(beta)=Im S-sum_i Re xi_i Im(partial_(xi_i)S)
                          -Re u Im(partial_u S).   (5.1)

Here beta is the actual crossing Bloch sum. To prove this,
write Log z_j=sum_i m_ji xi_i+m_ju u+i theta_j.
The Bloch--Wigner identity gives

    D(beta)=Im Phi+sum_j eps_j Re Log z_j Im Log(1-z_j).

Differentiation of Phi gives minus the corresponding linear
combinations of Log(1-z_j). Finally a real quadratic G with
purely imaginary linear term and real constant satisfies

    Im G=sum_i Re xi_i Im(partial_i G)+Re u Im(partial_u G).

Substitution proves (5.1). Compatible continuation of Li_2
and Log(1-z) preserves the identity: their monodromy terms
cancel in D, and their remaining constants are real.

Apply (4.2). All internal derivatives vanish on the branch,
and (4.4) yields

    Im S_flat=D(beta)+2 Re u Im v.                  (5.2)

At the complete color u=0 the previous fundamental-cycle
proof gives the fully calibrated value

    Im S_flat=Vol(M).                              (5.3)

Thus an admissible geometric action sheet of the actual
coefficients has the required exponential: for h=2pi*i/N,

    (2pi/N)log|exp(S_flat/h)|=Vol(M)                (5.4)

at the complete point. This evaluates the specified geometric
exponential. It is not an asymptotic formula for F_N(1).

## 6. The action period is the marked regulator norm

Define

    R_intr=S_flat-u v, U=2u, V=2v.

Equations (4.4) and (5.2) give exactly

    dR_intr=-(U dV-V dU)/4,
    Im R_intr=D(beta)+(Re U Im V-Re V Im U)/4.       (6.1)

Hence the period exp(2R_intr/(pi*i)), with the invariant
Heisenberg norm already fixed in the regulator note, satisfies

    log||P_intr||=2D(beta)/pi.                      (6.2)

There is no free imaginary additive constant: the retained
action and the exact identity (5.1) fix it. A real phase
constant remains part of the full complex-period comparison.

The functions in the geometric triangulation's full peripheral
rows are m=M^2,l=ell_intr^2. Indeed a peripheral matrix
diag(M,M^(-1)) fixing infinity acts on its horospherical
coordinate by multiplication by M^2, and similarly for the
longitude. Thus both the actual crossing sum and the positive
triangulation satisfy

    delta beta=-2M wedge ell_intr.

Their regulator difference has zero differential on the
connected geometric branch. It is zero at completeness by
the fundamental-cycle comparison. Therefore D(beta) is the
marked geometric regulator on that branch, on compatible
nondegenerate chart overlaps. Equations (6.1)--(6.2) identify
the connection and norm of its logarithmic action period.

At a complete longitude value -1, v may equal pi*i rather
than zero. Centering it requires the corresponding explicit
character in S_flat; the regulator line's deck multiplier
and invariant norm account for that change. It is not silently
replaced by a longitude value +1. Likewise the full ADO gauge
in Section 2 changes the classical shift sign; its meridian
germ remains a separate piece of the exact quantum pointing.

## 7. What this establishes, and the remaining theorem

There are now three actual-state comparisons:

1. The root-level meridian shift is the exact rational longitude
   insertion (1.2), with all endpoints, roots, and framing retained.
2. Its classical critical coordinate is the preferred longitude
   on the M-eigenflag, with the cut's inverse flag recorded.
3. The compatible geometric logarithmic action has the marked
   regulator connection and norm, and its complete imaginary
   value is Vol(M).

The selected finite period still needs a theorem showing a
nonzero geometric contribution of subexponential normalization,
and controlling the other contributions. An exponentiated
critical point, an allowed logarithmic character, and (5.3)
do not prove its coefficient in that period is nonzero.
They also do not prove a geometric factor in every minimal
annihilator of the actual sum. The root-level rational V=1
sector is not being equated with the geometric central curve.

The unchanged target is

    (4/N)log|F_N(1)|-log||P_hyp|| ->0.

No version of the original volume conjecture is asserted here.

## 8. Coverage and verification

Classical meridian/longitude potential interpretations already
have coverage in, for example,
[Sawabe, potential functions with arbitrary colors](https://msp.org/pjm/2023/322-1/pjm-v322-n1-p08-p.pdf).
The geometric action/regulator framework is also within the
previously recorded optimistic-limit coverage. The calculations
above were derived independently from the fixed actual weights;
no proof from those sources is a premise, and no novelty claim
is made for the classical conclusion.

The [audit](../experiments/audit_quantum_longitude_action.py) and
[results](../experiments/quantum_longitude_action_results.json)
check both rational eigenvector transports and the exact integer
telescoping identity; 53,262 local cancelled shift identities
at generic q and roots; and 80 inserted periods against the
independently assembled actual dense matrices. These include
the Kashaev color, both crossing signs, two successive shifts,
and even/composite levels. An exact trefoil calculation fixes
the longitude sign, inversion, and framing: the M-flag value
is -M^(-6), and the inverse flag has -M^6. It is a peripheral
calibration, not a torus-knot volume argument.

The actual positive and negative potentials satisfy (5.1) in
high-precision checks. A figure-eight complete/deformed
calibration in three frames checks the preferred-longitude
word, the five integer stationary windings, (5.2)--(6.2), and
the complete action value. The proofs are the rational and
logarithmic calculations above, not inference from these samples.
