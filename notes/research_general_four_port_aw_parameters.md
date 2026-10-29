# Research lead: generic four-port AW parameters, not a proved source kernel

29 October 2026. This preserves a possible extension of the completed
[physical tetrahedral source identity](actual_generic_trivalent_racah_source_identity.md).
It is NOT a proved formula for a general recoupling matrix, a root
positivity theorem, or an asymptotic input. No generic source gauge
or normalization has yet been established here.

Use generic q, Q=q^2, and ordinary four-port spin labels a,b,c,d.
The actual left and right intermediate ranges are

    e in [|a-b|,a+b] intersect [|c-d|,c+d],
    f in [|b-c|,b+c] intersect [|d-a|,d+a].

In the chamber c-d>=|a-b| put e_min=c-d,
e_max=min(a+b,c+d), f_max=a+d, and n=f_max-f. A candidate
for the finite operator parameters is

    A=q Q^(c-d), B=q Q^(b-a),
    C=q^-1 Q^(-c-d), D=q^-1 Q^(-a-b),
    z_e=q Q^e, kappa=q Q^(a+d), P=ABCD=Q^(-2(a+d)). (1)

For the finite symmetric polynomial operator

    Lg(z)=u(z)[g(Qz)-g(z)]+u(z^-1)[g(Q^-1z)-g(z)],
    u(z)=product_(T=A,B,C,D)(1-Tz)/[(1-z^2)(1-Qz^2)],

the eigenvalue polynomial is Lambda_n=(Q^-n-1)(1-PQ^(n-1)).
There is an elementary EXACT arithmetic identity

    kappa[Lambda_n+1+P/Q]
                 =q Q^f+q^-1 Q^-f, n=a+d-f.       (2)

The candidate forward coefficient vanishes at e_max, and the
backward coefficient vanishes at e_min. This explains the expected
support but does not identify the actual source recurrence.

The specialization a=b=d_phys/2, c=a_source, d=b_source, f=d_phys/2
gives precisely the parameters and physical Casimir eigenvalue in
the already PROVED generic six-head theorem. In that specialization
the polynomial degree is b_source, and the affine operator scale is
q^(d_phys+1)Q^b_source. This consistency check is not a general proof.

The remaining concrete steps would be: prove the actual general
Jacobi diagonal and off-diagonal product certificate from the typed
Fricke relations; derive its diagonal source gauge from the true
first-component-one Clebsch columns; and evaluate the actual endpoint
coefficient to fix normalization. The existing
[four-port kernel](actual_ordinary_four_port_recoupling_kernel.md)
already provides a finite two-sum formula with the correct cups and
cyclic clock, which would be the independent source to compare.
All generic high channels and pole-canceling root normals must be
retained before any specialization. Distinct spectra, formal matching
of (2), or named polynomial symmetry alone do not prove this bridge.
