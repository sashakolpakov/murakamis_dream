# A pointed Hermitian reflection for the actual cyclic source

29 October 2026. The phase-ratio double has a genuine source-compatible
realization: inverse conjugation of the quad coordinates is implemented
by an explicit ANTIUNITARY on the cyclic Fermat source, together with a
face swap. Its full normalizer is retained, and the construction is
valid at arbitrary radii. It agrees exactly with the pointed Fourier
quad rotations. It also extends to inhomogeneous cyclic packets, with
their source currents transformed rather than removed.

The same diagonal reflection fixes the actual fused arbitrary-plat
corner functional. Thus a whole original squared scalar has an exact
reflected doubled-word presentation. This does not yet identify its
contraction with a positive angle partition: the local joint spectral
source and all original sewing/co-source factors remain explicit.

## 1. Conventions and a radius-independent antiinvolution

Let N>=2, q=exp(pi i/N), Q=q^2. Use a sign sigma=+1 or -1 and set

    q_s=q^sigma, Q_s=Q^sigma,
    D_s e_a=Q_s^a e_a, S e_a=e_(a+1 modN),
    X=u D_s, Y=v S, B=I-X-Y.

The literal cap-source convention has sigma=+1. The cyclic quad
convention with Z_i Z_(i+1)=Q Z_(i+1)Z_i has sigma=-1. Define

    H_s(u,v)=(u',v')=(1/baru, q_s^(-1)barv/baru),
    A_(s,a)=(-q_s)^a Q_s^[a(a+1)/2],
    J_s=diag(A_(s,a)^(-1)), Theta_s=J_s conjugation.              (1)

All powers are ordinary integer expressions; no division by two
modulo N is used. Since A_(s,N)=1, the chirp is cyclic, including
its endpoint. It is unitary, Theta_s^2=I and H_s^2=id. If
u^N+v^N=1, then u'^N+v'^N=1. The central shape U=u^N is sent to
1/barU, which preserves the upper half-plane.

The exact matrix identity, with NO Fermat hypothesis, is

    B(u',v') J_s=-J_s barX^(-1) barB(u,v).         (2)

Indeed J_s S J_s^(-1)=-q_s^(-1)D_s^(-1)S; multiply barB on the
left by -barX^(-1) and use this equality. The extra invertible
left factor in (2) is not silently replaced by a similarity.

## 2. Actual right and left source frames, including their normalizers

Use the literal normalized frames from the cap/source construction,
with the indicated root orientation:

    F_a(u)=product_(r=1)^a(1-u Q_s^r),
    P_a(u,v)=v^a/F_a(u),
    L_a(u,v)=v^(-a)product_(r=0)^(a-1)(1-u Q_s^r),
    P_0=L_0=1.                                  (3)

They are the actual P,L of the cap theorem when sigma=+1. Whenever
these expressions are defined, finite-product reflection gives

    P(u',v')=J_s barP(u,v),
    L(u',v')=barL(u,v) D_s^(-1)J_s^(-1).          (4)

For the right formula factor each denominator as
1-baru^(-1)Q_s^r=-baru^(-1)Q_s^r(1-baru Q_s^(-r)).
Together with v'=q_s^(-1)barv/baru this gives precisely the
chirp in (1). The same calculation starting at r=0 gives the
COMPULSORY clock D_s^(-1) in the left formula.

Both transformations preserve the Euclidean norm in this cyclic
frame EXACTLY, at arbitrary radii. The cancellation uses the full
Fermat/shift normalizer v'. It is not a small-root-log argument.
For example |F_a(u)/F_a(1/baru)|=|u|^a can be exponentially large
when a is proportional to N, but the corresponding v-power
cancels it in (4). No assertion that a geometric clock radius is
1+O(1/N) is needed.

For an arbitrary retained operator C, the paired scalar identity is

    bar[L C P]=L(u',v') D_s
                    [J_s barC J_s^(-1)]P(u',v').                (5)

Thus the actual co-source carries a unitary clock insertion. It is
not merely the unshifted natural left source at the reflected point.
Every external scalar Gamma is conjugated and retained. In particular
Theta_s(Gamma P)=barGamma P'; it is not reset to one.

There is also an exact check on polynomial normalization. Let
Delta=1-u^N-v^N and Ptilde=F_d(u)P, d=N-1. Then

    B Ptilde=Delta e_0,
    Delta'=-barDelta/baru^N,
    F_d(u')=baru^(-d)barF_d(u),
    Ptilde(u',v')=baru^(-d)J_s barPtilde(u,v).     (6)

If the actual column is expressed in the polynomial Ptilde frame,
the power baru^d must therefore stay in its transformed Gamma.
It can be exponential; (4) does not license deleting it. The same
warning applies to the actual cap residue constants and Jacobians.
Those are retained by ordinary coordinate substitution. At a literal
corner Theta_s e_d=-q_s e_d and Theta_s e_0=e_0, so its pointed
normalization changes only by the specified unit phase, not an
unknown central normalizer.

## 3. Pointed quad rotations compose coherently

Use the original normalized Fourier matrix F_s and quad adapter

    (F_s)_(k,a)=Q_s^(ka)/sqrtN, W_s=F_s A_s,
    rho_s(u,v)=(q_s v/u,1/u).

Then EXACTLY

    Theta_s W_s Theta_s=W_s^(-1),
    H_s rho_s H_s=rho_s^(-1).                    (7)

The matrix proof is J_s barW_s barJ_s
=A_s^(-1)F_s^(-1)=W_s^(-1). The parameter proof is direct
substitution. No projective phase or central deck was discarded.
Using q instead of q_s^(-1) in (1) with sigma=+1 would insert
a root-of-unity deck; keeping the orientation makes (7) exact.

If W_s P(p)=c(p)P(rho_s p) is the actual pointed source rotation,
P_0=1 fixes c. Equations (4),(7) force

    c(H_s rho_s p) barc(p)=1.                    (8)

Thus the exact source Gamma of a reflected pointed rotation is
its reciprocal conjugate, including its nontrivial modulus. This
is a genuine normalization identity, not a new unit-norm choice.
The left-source clock in (4), and the corresponding clock in (5),
must still be used on sewn output faces.

## 4. Full currents survive the reflection

For ANY inhomogeneous packet B f=eta, (2) gives

    B' Theta_s f=-Theta_s(X^(-1)eta).              (9)

When B is invertible this is also an exact resolvent identity;
meromorphic continuation keeps its poles and residues. It neither
sets Delta=0 nor deletes a current proportional to Delta. Thus a
local source decomposition into a balanced residue and a current
is reflected LINEARLY with both parts retained.

For example the complete Newton packet f_j=B_N(u,vQ^j) obeys
(I-uR+vD_Q R)f=(1-u^N+v^N)1, with (Rf)_j=f_(j+1).
The two terms uR and -vD_Q R form a finite Weyl pair, of central
powers u^N and -v^N. A fixed unitary Weyl change puts it in the
form of (9). Its source must undergo the SAME change and the
factor X^(-1) in (9); no claim that the reflected packet is the
same standard B_N with its source reset is made. In particular
this is not a proof that the inhomogeneous beta current vanishes.
The full-Psi split and its marked scalar normalizer remain part
of the original packet.

## 5. The inverse-reflected triad and its positive joint basis

Put

    Z0=X, Z1=Y^(-1), Z2=-X^(-1)Y.

Their cyclic commutation parameter is Q_s^(-1), and their ordered
product is -Q_s^(-1). At the reflected point,

    (Z0',Z1',Z2')=
       (J_s barZ0^(-1)J_s^(-1),
        J_s barZ2^(-1)J_s^(-1),
        J_s barZ1^(-1)J_s^(-1)).                 (10)

Thus inverse conjugation comes with the 1<->2 face swap. The
unitary map I tensor J_s takes P tensor barP to P tensor P'
and takes the phase-ratio observables Z_i tensor barZ_i^(-1)
to Z_i tensor Z'_(tau(i)), tau=(1 2). This is a source-compatible
interpretation of the inverse factor, not arbitrary inversion of
the original bra.

For sigma=-1 the phase-ratio observables commute, are unitary
even for complex u,v, and have ordered product Q. A joint
orthonormal basis is

    |s,r>=N^(-1/2)sum_a Q^(ra)|a,s-a moduloN>.

Its first two eigenvalues are (u/baru)Q^(-s) and
(barv/v)Q^r; the third is Q divided by their product. This gives
a genuine positive joint spectral norm. It is not yet a positive
angle state or its geometric edge projector.

Indeed the ORIGINAL conjugate source in this basis has coefficients

    c_(s,r)=N^(-1/2)sum_a Q^(-ra)P_a barP_(s-a).                 (11)

The two source equations, BEFORE any positivity or projection,
imply on the Fermat locus

    c_(s,r+1)=[1-(v/barv)Q^(-r)]
              /[u-(v/barv)baru Q^(s-r)] c_(s,r).                (12)

On the open family with Im(u^N)>0 and principal root marks
u=(u^N)^(1/N),v=(1-u^N)^(1/N), every factor in (12) is nonzero.
To check it, write alpha=Arg(u^N)>0,beta=Arg(v^N)<0. The
third positive central quad angle gives -pi<beta-alpha<0.
Neither beta nor beta-alpha is a multiple of pi. For each fixed
s the Fourier transform in (11) is not identically zero, since
all P_a barP_(s-a) are nonzero. Equation (12) therefore proves
that EVERY c_(s,r) is nonzero at every N.

Here u^N is a Frobenius center, not a claim about a fixed
semiclassical clock radius. No tame geometric-contour estimate
is inferred from choosing this center independent of N.

In particular the positive half-phase square roots do not
automatically select one affine tetrahedral charge. For this
open family write alpha_i for the three positive CENTRAL quad
arguments, sum alpha_i=pi, and let

    r0=-s modN, r1=r, r2=s-r modN, 0<=ri<N.

The inverse-ratio upper-half-plane square roots have angles
beta_i=pi-(alpha_i+pi ri)/N. Their product is q^d on the
sum ri=0 or2N sectors and q^(-1) on the sum ri=N sector.
Both occur with NONZERO source coefficients. Only the sum2N
sector has sum beta_i=pi*d/N; the sum0 sector has sum
3pi-pi/N. Extra physical windows or source constraints are
therefore indispensable. They cannot be inferred from the
commuting phase-ratio algebra alone.

A proposed local Cauchy norm supported ONLY on the desired
angle sector is not continuous on this whole cyclic source:
a discarded Bell basis vector has zero proposed norm but a
nonzero source pairing in (11). This rules out that unqualified
ALL-EXTERIOR local norm substitution, not a global comparison
after the actual co-source or compensated length metric is used.

## 6. The whole original pointed scalar has a reflected double

Use the already proved arbitrary-plat fused source

    K_N=chi_N N^(1-k) <e_out|B_beta|e_in>.

Each input pair is (d,0); each ordinary output pair is (0,d),
and the marked output pair is (d,0). On EVERY such pair the
eigenvalue of J_s tensor J_s is J_(s,d)J_(s,0)=-q_s.
Consequently the input and output corner eigenvalues of
J_tot=J_s^(tensor2k) are equal. Hence EXACTLY

    barK_N=barChi_N N^(1-k)
       <e_out|J_tot barB_beta J_tot^(-1)|e_in>.                  (13)

This proves a source-exact reflected doubled-word presentation
of |K_N|^2, with no normalization by an unknown period. All
kernel currents, original Cartan factors and external lines
are conjugated and retained. On every standard cyclic quad
chart, (10) identifies the inverse-reflected variables; (7)
makes the pointed S3 changes compatible.

It does not prove that every global cyclic/cluster adapter is
unitary, or that all geometric edge isotypic constraints have
been selected by this source. If an ordered edge word is
reflected with reversed face order, its character transforms
chi_e to 1/barchi_e. Existing UNIT characters, including the
desired full-clock character, are preserved; a free character
has not thereby been chosen. Nor may an exponentially
conditioned physical-to-cyclic frame be discarded. The
unitarity assertions here are in the specified cyclic flat
metric, with the actual source/co-source transformed together.

Thus the reflection is a constructive norm-compatible piece
of a special-inner-product comparison. A positive angle
majorant still requires the actual geometric tensor/wiring
map and its controlled current or defect estimate.

[Audit](../experiments/audit_phase_ratio_fermat_source.py): exact
reflected generators and sources, arbitrary-radius and
inhomogeneous normalizers, pointed dihedral identities,
phase-ratio spectra/source recurrence, and original complete
signed plat sources.
