# Exact Ward cancellation of cyclic wall currents, with the marked charge retained

28 October 2026. The original all-plat Ward corner has an explicit
co-source homotopy. Under cyclic completion it produces a rank-two
commutator wall current. That current is canceled exactly by the
corresponding sewing defect, before asymptotics or closure. For an
assembled word the typed defects telescope.

This gives a finite relative-cycle comparison for the Ward reduction;
it does not identify nonlinear positive-angle boundary prisms with
those currents. The surviving marked wall has charge one. It is not
permitted to delete the only source carrier.

## 1. An explicit original co-source homotopy

Use the literal arbitrary-plat conventions in
[the Rogers transport theorem](actual_rogers_bridge_transport.md).
Put d=N-1. After the k-1 ordinary caps the remaining dual pair has
total integer degree d. On that fiber let

    p=|d,0>, ell=<d,0|,
    mu(a)=x^(d-a)(-1)^a Q^(-a(a+1)/2) F_a^2/N^2.

The first color x here is the remaining pair's actual color. In
particular mu(d)=1. Let F_rel=S_a be the ACTUAL total lowering
operator in fusion coordinates. It sends the degree-d fiber to
degree d+1. Define a row on the latter fiber by

    nu(a+1,d-a)=mu(a), 0<=a<d.

Then, on the entire degree-d fiber, exactly

    mu-ell=nu F_rel.                                      (1)

This is an actual co-source homotopy, not just vanishing on a
single vector. Since the full original remaining vector v satisfies
F_rel v=0, equation (1) proves mu v=ell v. It is the explicit
current behind the Ward corner. All meridian powers in mu and nu
remain functions.

For a general nonintertwining coupon or a separated cyclic sector,
F_rel v need not vanish. Its omitted term is precisely nu F_rel v.

## 2. Cyclic completion has a rank-two Ward defect

Consider the positive actual Euler transfer

    T=a J_+ tensor J_-, A=a S tensor S^-1,

with the literal truncated shifts J and cyclic S. The two residue
fibers relevant to F_rel are k=d and k=0. In either cyclic basis
the operator A is aS. Between them F_rel is the strict raising
shift J_+. Consequently its typed cyclic defect is

    Delta=F_rel A_in-A_out F_rel
         =a (|1><d|-|0><d-1|).                            (2)

For N=2 this is the same two distinct matrix units; no generic
rank assertion or separated-wall assumption is required.

The ACTUAL transfer has no such defect:

    F_rel T_in=T_out F_rel,

because J_+ on the first head commutes with J_+ tensor J_-.
Writing R_A=(t-A)^(-1), R_T=(t-T)^(-1), and E=R_T-R_A,
the resolvent identity gives the exact rational equations

    F_rel R_A,in-R_A,out F_rel=R_A,out Delta R_A,in,

    F_rel E_in-E_out F_rel=-R_A,out Delta R_A,in.           (3)

Thus the cyclic Ward defect and its sewing Ward defect cancel
POINTWISE. This is more than equality after a particular trace.
The full central polynomial t^N-a^N and its poles remain in (3).
On a cut meeting such poles one must use the matched residue and
finite-part prescription already proved in
[the sewing cycle theorem](cyclic_sewing_regularized_cut_cycle.md).
Equation (3) does not authorize retaining only the old branch cuts.

Every common Cartan line multiplies the same two equations. The
negative crossing and other residue fibers have the same typed
identity with their literal operators; no replacement inverse or
scalar normalization is used.

## 3. The full original marker detects the Ward current

For one actual dual cup, input colors are (x,y), y=x^(-1)Q^(-1),
and the checked positive core is D u_N(aJ_+ tensor J_-) with
a=x^(-1). The output marked row is mu_y. The Gaussian D depends
only on the second head, so it commutes with F_rel as a typed map.

Since T p=0, the original marked resolvent is exactly

    mu_y D R_T,in(t) p=1/t.                               (4)

Thus every holomorphic functional-calculus germ f gives the
original value f(0). In particular the actual Euler germ has
f(0)=1. Together with the original Cartan/framing line this is
the original one-bridge normalization, not a newly assigned scalar.

Set g_mu=mu_y D R_A,in p and g_ell=ell R_A,in p. Equation (1)
and the first equation of (3), with F_rel p=0, give

    g_mu-g_ell=nu D_out R_A,out Delta R_A,in p.            (5)

This is the exact missing current when somebody applies the Ward
corner separately to a cyclic sector. The right-hand side can be
nonzero and has source-visible cyclic poles.

The corner cyclic term is especially simple:

    g_ell=t^(N-1)/(t^N-a^N).

Its marked relative wall is

    1/t-g_ell=-a^N/[t(t^N-a^N)].                          (6)

Its residue at zero is one, its residues at the N cyclic poles
are -1/N each, and it has zero residue at infinity. Hence even
after full zero-current Ward reduction a nonzero augmented wall
survives. A source-free cyclic resolvent is holomorphic at zero
and has zero original small-circle period. It cannot be the
replacement for (4) with the wall removed.

## 4. Exact residue contraction with polynomial cost

Let beta_j=aQ^j. In the input fiber write S for its cyclic shift,
and put

    c_r=mu_y D S^r p, 0<=r<N, c_0=1.

The original cyclic residues are exactly

    w_j=Res_(beta_j) g_mu(t)dt
       =(1/N)sum_(r=0)^(N-1)c_r Q^(-jr),
    sum_j w_j=1.                                         (7)

The corner residues are 1/N. Their difference is an explicit cyclic
boundary. With (S_res J)_j=J_(j+1), put

    J_j=(1/N)sum_(r=1)^(N-1)
                    c_r Q^(-jr)/(Q^(-r)-1).

Then

    (S_res-1)J=w-(1/N)1.                                 (8)

The zero-average inverse H of S_res-1 satisfies the genuine chain
contraction

    Delta_res H=H Delta_res=I-Pi_0,
    ||H||_(ell2)<=1/[2sin(pi/N)]<=N/4,
    ||H||_(ell-infinity)<=N.                              (9)

These are the flat norms on the ACTUAL scalar cyclic-residue coordinates
j=0,...,N-1. They are not norms asserted invariant under an exponentially
conditioned fusion frame. The first bound is the unitary Fourier spectral calculation. For
the second, a zero-sum input g has a cumulative primitive
P_j=sum_(h<j)g_h. Both j and N-j bound its absolute size, so
|P_j|<=N||g||_infinity/2. Subtract its mean to impose zero
average. This proves the stated N bound. No inverse is applied
to the constant character; Pi_0 retains its marked augmentation.

Equations (5)--(9) are an actual Ward/cyclic residue comparison.
With a nonconstant analytic test function f, summation by parts
retains the dual difference of f, and its cut/pole terms. Thus
(8) does not permit deleting these currents before their full
relative pairing. For f=1 all nonconstant residues cancel exactly.

## 5. Large individual residues occur in this original unit source

At the canonical unit root and any unit meridian, for 1<=r<N,

    |c_r|=|F_(r-1)|^2/N^2.                                (10)

Indeed S^r p has first index r-1 and second index N-r;
the Gaussian has modulus one, and the actual marked row is
mu_y(n)=y^(d-n)|F_n|^2/N^2. This also proves uniformity over
all unit meridians, not only one complete numerical value.

Finite Fourier inversion gives the two-sided inequalities

    (max_r |c_r|)/N <= max_j |w_j| <= max_r |c_r|.

The already independently proved figure-eight factorial estimate
therefore yields

    lim_N (1/N)log max_j|w_j|=Vol(4_1)/(2pi)>0,            (11)

whereas sum_j w_j is EXACTLY one. This is an original-source
cancellation example satisfying all the actual zero-current Ward
equations. It is neither an arbitrary normalization counterexample
nor a claim that this unknot has positive volume.

The polynomial homotopy bound (9) is entirely compatible with
(11): it controls the cost relative to the original coefficient
norm; it does not replace exponential input coefficients by
polynomial ones without their exact cancellation.

## 6. Whole-word cancellation and the precise surviving class

For arbitrary finite typed factors O_j:V_(j-1)->V_j, retain the
actual transported lowering operators F_j and define

    delta_j=F_j O_j-O_j F_(j-1).

Their original ordered product W obeys the exact identity

    F_L W-W F_0
       =sum_j O_L...O_(j+1) delta_j O_(j-1)...O_1.         (12)

The original cups have F_0 p=0; the original assembled word and
ordinary caps intertwine. Therefore the TOTAL co-source change
from mu to the Ward corner is zero. In a cyclic/sewn realization
(3) supplies the local rational defect cancellation. With its
complete matched contours, every cyclic residue and ramified
finite-part contribution is carried through (12). This statement
is linear in the exact rational forms and does not assume an
unmarked deformation of a small circle into branch cuts.

It follows that the FULL original fused corner can use the
purely cyclic cross-sewing representation with its explicit
relative boundary source. This is obtained by applying the Ward
co-source homotopy to the assembled original network and then
the local exact resolvent expansion, or by retaining all the
currents in the opposite order; (3) and (12) equate the procedures.
The total sum of marker-reduction Ward currents is removable.
The unit augmented class (6) is NOT removable. In particular a
sectorwise corner replacement without (5) is not this theorem.

All of (1)--(12) are covariant under a literal full tensor/frame
change, with F, the source, every sewing map and every current
transformed together. An isomorphism of cyclic kernel lines alone
does not supply that full change. In particular this note does not
identify arbitrary nonlinear positive-quad angular boundary prisms
with the currents in (12), nor prove that the retained cusp class
couples to a geometric critical point.

The complementary [compactified quad transport](cap_wall_fermat_quad_residue_transport.md)
constructs an actual divisor-residue image of the cup. That local
transition can carry the augmentation; it must still respect the
cyclic-pole and source-current data above in a whole positive
chart comparison.

[Original-matrix and wall-current audit](../experiments/audit_ward_cyclic_wall_contraction.py).

The audit passes fourteen original complete/generic dual-cup families,
twelve assembled two- and three-slot original Euler words with every
cyclic/sewing sector retained, eight chain-contraction norm cases, and
six source-scale grids through N=1280. In the assembled words the
separate marker changes are nonzero, their commutator-current sum is
exactly zero, and the original unit source is retained. The proofs above
are uniform; these finite tests independently fix operator order and
the two different residue fibers in (3) and (5).
