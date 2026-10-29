# The complete original source has a conserved indefinite form and an explicit positive Cauchy metric

29 October 2026. On the COMPLETE N-dimensional three-head source
multiplicity, both actual braid generators preserve one explicit
indefinite Hermitian form. The original cup is null for this form and
the ordinary cap is its prescribed dual. A different, full-rank positive
Hermite metric has polynomial BOTH original boundary norms. Thus a
special-inner-product Cauchy estimate is now literal for this complete
source; the missing sharp statement is its coherent WORD ENERGY bound,
not the Cauchy inequality or a boundary-normalization choice.

## 1. Complete module and literal sources

Use N>=2, d=N-1, q=exp(pi i/N), Q=q^2, x=-q^(-1)=q^d,
F_j=(Q;Q)_j. The
[complete source theorem](actual_complete_source_multiplicity_module.md)
identifies the actual three-head Hopf multiplicities with
W=(V tensor V)_(integer degree d), basis e_u=|u,d-u>.
There are N multiplicities; all value and Jordan-derivative channels
remain. On W put A=Omega_12 and B=Omega_23. Explicitly,

    A_(u,u)=q+q^(-1)-q(1-Q^u)^2-q^(-1)(1-Q^(u+1))^2,
    A_(u-1,u)=A_(u,u-1)=-(1-Q^u)^2,
    B e_u=c_u e_u+b_u e_(u-1),
    c_u=q^(2u+1)+q^(-2u-1), b_u=Q^u+Q^(-u)-2.       (1)

Missing endpoint arrows vanish. The ACTUAL crossings on this entire
module are R_12=kappa r_N(A), R_23=kappa r_N(B), with their literal
inverses. The original common Cartan kappa=q^(d^2/2) is retained.
The polynomial r_N has unit nodal values nu_j and the actual Hermite
jets; no semisimple truncation is used.

The original boundary vectors are

    p_u=N x^(u-d), ell_u=x^(-u)Q^(-u)/N,
    m_u=x^(d-u)/N^2.                                    (2)

The marked row here is only its degree-d restriction. Arbitrary marked
exteriors retain the full matrix-valued functional in the source theorem.
For an original cup--three-head-word--ordinary-cap tangle, closed by
the prescribed cut of value one on I, its exact scalar is

    K_N=chi_N ell W p.                                  (3)

The full even-plat source theorem states when this scalar presentation
applies; inserted nonintertwining exteriors are not replaced by (3).
All original framing and modified-dimension factors stay in chi_N.

## 2. An actual common Hermitian form on ALL channels

Let P be physical index reversal, P_(u,v)=delta_(u+v,d). It is a
Hermitian unitary involution, with both positive and negative eigenvalues.
Directly from (1),

    A^*P=PA, B^*P=PB.                                  (4)

For A, complex conjugation replaces Q by Q^(-1), and reversal takes
each adjacent entry to that conjugate entry. Its diagonal behaves the
same way. A is complex symmetric. For B its entries are real, while
c_(d-u)=c_u and b_(N-u)=b_u give PBP=B^T. These proofs include
both physical endpoints and all level parities.

At each real double node c_j the actual crossing polynomial satisfies

    |r_N(c_j)|=1, r_N'(c_j)/r_N(c_j) purely imaginary.

At the possible simple node only the first condition is required.
Therefore bar(r_N)r_N-1 vanishes with the full multiplicity of
P_N=T_N+2. The polynomial identity P_N(A)=P_N(B)=0 and (4) imply

    R_i^* P R_i=P, i=12,23.                            (5)

The unit Cartan |kappa|=1 is included. This is an exact Hermite
functional-calculus argument, including every nilpotent derivative.
Consequently EVERY signed original word W preserves P on this complete
module. It is not merely a leading semiclassical conservation law.

The original sources themselves obey

    ell=p^*P/N^2, p^*Pp=0, m=p^*/N^3.                  (6)

Thus (3) is chi_N p^*P Wp/N^2, an indefinite matrix coefficient
between actual null source vectors. This does not make it a positive
norm. The ordinary cup--cap bubble is still zero.

For completeness a SOURCE-UNITARY coordinate system displays both
the full dynamics and the cut. Let

    U_(u,k)=N^(-1/2)x^(u-d)Q^(-ku), D_(k,k)=q^k,
    V_0=U D^(-1), A_0=V_0^* A V_0, B_0=V_0^* B V_0.

The orientation D^(-1) on the physical basis columns is compulsory.
The exact nonzero entries are

    A_0|k>=c_k|k>+8sin^2(pi k/N)|k-1>
                         +(c_(k-1)-c_0)|k-2>,
    B_0|k>=(1-Q^(-k))|k-1>+2q^(-2k-1)|k>
                              +(1-Q^(-k-1))|k+1>.        (7)

The coefficients kill all would-be wraps at k=0,1,d. In particular
||A_0||<=14 and ||B_0||<=6 uniformly in N. This does not bound the
high-degree functions r_N(A_0),r_N(B_0).
The transformed P is (-1)^d times index reversal, and

    V_0^*p=N^(3/2)e_0, ell V_0=(-1)^d N^(-1/2)e_d^T,
    m V_0=N^(-3/2)e_0^T,
    K_N=chi_N(-1)^d N (W_0)_(d,0).                    (8)

Thus this coordinate change has no exponential frame or source cost.

## 3. What positive Cauchy says, with its exact source cost

For EVERY prescribed positive Hermitian G on W, actual Cauchy gives

    |K_N|^2<=|chi_N|^2 (ell G^(-1)ell^*)
                                      ((Wp)^*G(Wp)).     (9)

This uses the coherent vector Wp, not separately squared paths. A
positive metric cannot be replaced by the conserved indefinite P.

There is a useful optional source-balancing condition

    GPG=P, equivalently G^(-1)=PGP.                    (10)

Then (6) gives the exact dual-source identity

    ell G^(-1)ell^*=p^*Gp/N^4.                        (11)

Equation (9) has now balanced the actual source and co-source with
one positive metric. Such metrics exist (I is one), but existence
does not prove that the transported energy is geometrically small.

For reference, any positive H yields a canonical P-compatible metric

    G=H^(1/2)|H^(-1/2)PH^(-1/2)|H^(1/2).              (12)

Indeed if C=H^(-1/2)PH^(-1/2), then
H^(1/2)PH^(1/2)=C^(-1), and |C|C^(-1)|C|=C proves
(10). This replacement can change energies exponentially; no tame
comparison with a proposed geometric H is inferred from (12).
Nor is the following actual Hermite metric assumed to satisfy (10).

## 4. A COMPLETE positive metric already controls both boundaries

Let J be the specified complete anti-Pascal recoupling, and V_H the
complete degree-d Hermite frame for A from
[the all-channel packet theorem](actual_complete_casimir_hermite_packet.md).
Keep its full bilinear Christoffel--Darboux inverse, including all
derivative columns. Put

    L=V_H^(-1)J, G_0=L^*L/N,
    u=Lp, a=ell L^(-1), W_ch=L W L^(-1).              (13)

This is a full-rank positive Hermitian metric specified before the
word W, without an unknown knot scalar. The exact original sources
in each double channel c are

    u=N(-1)^d x^(-d)(-c,4-c^2),
    a=(x^d/N)(1,0).                                 (14)

At the possible simple node, u=Nx^(-d), a=x^d/N. These are the
source theorem's complete CD/Chebyshev simplification; the potentially
large crossing derivative cancels in the source value entry.
Writing n_distinct=ceil(N/2), it gives

    ell G_0^(-1)ell^*=N||a||^2=n_distinct/N<=1,
    p^*G_0p=||u||^2/N<=8N^2.                         (15)

The last constant includes N=2. All normalizer phases in (14) remain.
Thus (9) becomes the explicit ORIGINAL-SOURCE positive-energy bound

    |K_N|^2<=|chi_N|^2 (n_distinct/N) E_N(W),
    E_N(W)=||W_ch u||^2/N=(Wp)^*G_0(Wp).             (16)

All mixed channel copies remain inside this norm. No dephasing or
replacement of the full marked source is used. This is precisely
Cauchy in a special positive inner product, with controlled actual
boundary costs on the COMPLETE module, not only its c_0 plane.

The desired geometric comparison for this PARTICULAR fixed metric is

    |chi_N|^2 E_N(W)<=exp(o(N)) Z_N(geometric angles).  (17)

It is now [proved false for the original figure-eight](actual_figure_eight_complete_channel_energy.md):
an exact complete channel forces excessive energy at every odd level.
The [terminal coherent Gram](actual_terminal_packet_positive_gram.md)
supplies a different positive metric on the same full module, with
sharp benchmark energy and an all-width Cauchy construction; its
general-prefix energy remains open. The Hermite-diagonal braid has
polynomial jets, but its conjugate through the full Racah matrix has
the displayed excess. P-conservation does not imply (17). Making G depend on the
completed unknown W to force constant energy merely moves that same
quantity into the dual boundary cost. Thus the actual metric and
boundary reduction are constructive; the sharp word-energy estimate
is a distinct mathematical step, not a consequence of Cauchy alone.

[Audit](../experiments/audit_actual_complete_source_krein_cauchy.py):
literal original full-Cartan pair crossing, complete anti-Pascal
recoupling, both P-unitary generators, all source phases and unitary
Fourier endpoints, full Hermite-source normalizers, and actual coherent
word Cauchy energies in positive and P-compatible metrics.

Fresh replay: PASS twelve complete original Casimir/braid/source modules,
including the full Hermite boundary metric, coherent signed-word Cauchy
energy and non-diagonal P-compatible positive metrics. Compilation passes.
